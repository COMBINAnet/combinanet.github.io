#!/usr/bin/env python3
"""
Classify lychee link-check results using the two-tier policy defined in
broken-links.yml.

Policy summary
--------------
Domains listed in BOT_PROTECTED_DOMAINS have HTTP 403 / 429 responses
downgraded to *warnings* rather than hard failures, because those domains
are known to block automated checkers.  Every other failure code — including
404, 410, 5xx, TLS/DNS errors, and connection timeouts — remains a hard
failure even for listed domains.  This keeps the checker useful for detecting
real breakage while avoiding spurious CI failures caused by bot-blocking.

Exception governance
--------------------
- Exceptions are domain-specific and limited to HTTP 403 and 429 only.
- Each entry must have a comment explaining why it is listed.
- Review at least once a year; remove entries that are no longer needed.
- Note any addition or removal in the PR description.

Exit codes
----------
0  All links OK, or only bot-block warnings.
1  One or more hard failures found.
"""

import json
import os
import sys
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Bot-protected domain exceptions
# ---------------------------------------------------------------------------
# fmt: off
BOT_PROTECTED_DOMAINS = {
    "stri.si.edu",  # Smithsonian Tropical Research Institute blocks bots with 403
}
# fmt: on

RESULTS_FILE = "lychee-results.json"


def get_domain(url: str) -> str:
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ""


def is_bot_protected(url: str) -> bool:
    domain = get_domain(url)
    return any(
        domain == d or domain.endswith("." + d) for d in BOT_PROTECTED_DOMAINS
    )


def extract_status_code(status):
    """Return the HTTP status code from lychee's JSON status field.

    Lychee serialises Status in several possible shapes depending on version:
      {"code": 404, "text": "Not Found"}   — flat object
      {"Fail": 404}                         — enum variant with bare int
      {"Fail": {"code": 404}}               — enum variant with nested object
      404                                   — bare integer
    This function handles all known variants defensively.
    """
    if isinstance(status, int):
        return status
    if isinstance(status, dict):
        if "code" in status:
            val = status["code"]
            return int(val) if isinstance(val, (int, float)) else None
        # Enum-variant shapes: {"SomeVariant": <int or dict>}
        for val in status.values():
            if isinstance(val, int):
                return val
            if isinstance(val, dict):
                code = val.get("code")
                if isinstance(code, (int, float)):
                    return int(code)
    return None


def parse_link(link):
    """Return (url, status_code) from a single lychee link entry.

    Lychee may emit each entry as a dict {"url": ..., "status": ...}
    or as an array [url, status, source].
    """
    if isinstance(link, dict):
        return link.get("url", ""), extract_status_code(link.get("status"))
    if isinstance(link, (list, tuple)) and len(link) >= 2:
        return str(link[0]), extract_status_code(link[1])
    return str(link), None


def load_results(path: str) -> dict:
    try:
        with open(path) as fh:
            return json.load(fh)
    except FileNotFoundError:
        print(f"Results file '{path}' not found; assuming lychee did not run.")
        sys.exit(0)
    except json.JSONDecodeError as exc:
        print(f"Could not parse lychee results JSON: {exc}")
        sys.exit(1)


def classify(data: dict):
    """Return (hard_failures, warnings) as lists of (url, code, source)."""
    hard_failures = []
    warnings = []

    # fail_map:  HTTP-level failures (4xx, 5xx, unexpected codes)
    # error_map: transport-level failures (DNS, TLS, timeout, connection refused)
    combined = {}
    combined.update(data.get("fail_map", {}))
    combined.update(data.get("error_map", {}))

    for source, links in combined.items():
        for link in links:
            url, code = parse_link(link)
            if is_bot_protected(url) and code in (403, 429):
                warnings.append((url, code, source))
            else:
                hard_failures.append((url, code, source))

    return hard_failures, warnings


def write_summary(hard_failures: list, warnings: list) -> None:
    lines = ["## 🔗 Link Check Results\n\n"]

    if hard_failures:
        lines.append(f"### ❌ Hard failures ({len(hard_failures)})\n\n")
        lines.append("| URL | Status | Source |\n|---|---|---|\n")
        for url, code, src in hard_failures:
            lines.append(f"| `{url}` | {code if code else 'error'} | `{src}` |\n")
        lines.append("\n")

    if warnings:
        lines.append(
            f"### ⚠️ Warnings — bot-blocked domain(s) ({len(warnings)})\n\n"
        )
        lines.append(
            "These URLs returned 403 or 429 from a domain known to block automated "
            "checkers. They are listed here for visibility but **do not fail the "
            "job**. If a URL looks wrong, verify it manually in a browser and update "
            "the source file if it is truly broken.\n\n"
        )
        lines.append("| URL | Status | Source |\n|---|---|---|\n")
        for url, code, src in warnings:
            lines.append(f"| `{url}` | {code if code else 'error'} | `{src}` |\n")
        lines.append("\n")

    if not hard_failures and not warnings:
        lines.append("### ✅ All links healthy\n")
    elif not hard_failures:
        lines.append("### ✅ No hard failures\n")

    text = "".join(lines)
    print(text)

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if summary_file:
        with open(summary_file, "a") as fh:
            fh.write(text)


def main() -> None:
    data = load_results(RESULTS_FILE)
    hard_failures, warnings = classify(data)
    write_summary(hard_failures, warnings)

    if hard_failures:
        print(f"FAIL: {len(hard_failures)} hard link failure(s). See summary above.")
        sys.exit(1)

    if warnings:
        print(
            f"PASS with {len(warnings)} warning(s): "
            "bot-blocked URL(s) could not be verified automatically."
        )
    else:
        print("PASS: All links OK.")


if __name__ == "__main__":
    main()
