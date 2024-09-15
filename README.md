# COMBINA website

The site uses the [al-folio](https://github.com/alshedivat/al-folio) theme for [Jekyll](https://jekyllrb.com/docs/Jekyll), significantly customized with inspiration from [Decision Lab UCSF](https://decisionlab.ucsf.edu/) and [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).

## Basics of updating site content

There are a few different kinds of content updates you might need to make:

- [Update pages that appear in the main navigation](#how-to-update-pages)
- [Update individual "resources" or "opportunities" items](#how-to-update-collection-items)
- [Update information about people](#how-to-update-or-add-people)
<!-- - [Add news posts](#how-to-add-news-posts) -->
<!-- - [Add publications](#how-to-update-the-publication-list) -->

Before making any content updates, you'll need to understand a little about: 

### GitHub

Think of GitHub as being like supercharged Google Docs for code. 
Multiple people can work on the same code, it keeps track of who made what changes and when, it's easy to reverse changes that have been made, and different versions can be developed at the same time.

If you're totally new, try completing the "First Day on GitHub" curriculum at [GitHub Skills](https://skills.github.com/).
These interactive tutorials take place on GitHub itself and cover the core skills you'll need.

### Jekyll

The files in this repository are building blocks for the website, but they are not what actually gets served in the live site. 
The Jekyll software takes the building blocks and processes them into the finished website. 
This processing step happens automatically every time you commit changes to the `main` branch of this repo.

The finished website files live on the automatically-generated `gh-pages` branch of the repo. 
You can switch to that branch to see how different those files look from the source files on `main`.
**You should never commit any changes directly to `gh-pages`**.
It gets completely deleted and re-created every time a new commit is made to `main`.

### Markdown and YAML

Instead of directly editing in HTML, you'll usually be giving Jekyll information in two human-readable plain-text formats. 

#### Markdown

This README.md file is written in Markdown. 
Markdown allows for simple formatting like **bold** (double asterisks: `**bold**`), *italics* (single asterisks: `*italics*`), and [hyperlinks](https://www.marinebiosecurity.net) (put the linked text in square brackets immediately followed by the address in parentheses, like: `[hyperlinks](https://www.marinebiosecurity.net)`). 
See [this cheatsheet](https://www.markdownguide.org/cheat-sheet/) for more details.
You can also check out the markdown in this README file by opening [combinanet.github.io/README.md](https://github.com/decisionlabucsf/decisionlabucsf.github.io/blob/master/README.md) and clicking "Code".

#### YAML

YAML is a structured data format that uses space-indents (_never_ tab-indents!) to show structure and uses colons to associate fields with values. For example:

```yaml
- name: Charles Darwin
  position: Naturalist
  affiliation: H.M.S. Beagle

- name: Charles Elton
  position: Senior Fellow
  affiliation: Corpus Christi College in the University of Oxford
```
This list has two entries. Each entry has fields for name, position, and affiliation. 
Note that you don't have to put text strings within quotation marks, unless they contain characters with special meaning in YAML, such as colons or quotation marks.

```yaml
darwin:
  fullname: Charles Darwin
  position: Naturalist
  affiliation: H.M.S. Beagle

elton:
  fullname: Charles Elton
  position: Senior Fellow
  affiliation: Corpus Christi College in the University of Oxford
```
  
This is also a list with two entries, however, now each entry has a name (a "key", in YAML-speak).
Each entry still has 3 fields, for full name, position, and affiliation.
The difference between this list and the first one is that entries in this list can be directly located by name, whereas the only way to find entries in the first list is to check each one in turn.

When editing site content that's stored as YAML, all you need to know is that you should make sure to keep whatever list you're editing in the **same format** as you found it — switching from un-named entries to named entries (or vice versa) will confuse the software that ingests the information.

YAML is very sensitive to correct indentation.
If you're struggling to get some YAML to do what you want, try pasting it into [YAML Checker](https://yamlchecker.com/) for feedback on what might be wrong.
    
## How to update pages

Every page that appears in the main site navigation is created from a Markdown file that lives in the `_pages` folder.
In many cases, what you want to edit might be data in the YAML "preamble" (section that comes at the beginning of the Markdown file) rather than in the file itself.

For pages that list items in a "collection" (e.g., Opportunities, Resources), the contents are generated automatically, so there won't be much to edit directly.
To edit items that appear on these pages, you'll need to edit the individual Markdown files that represent the items (see the next section!).

## How to update collection items

A "collection" is a way of telling Jekyll about how your site content is organized.
Each item in a collection is represented by a single Markdown file.
This file might have lots of Markdown in it, or it might just be a YAML header with no Markdown content at all.

Collection items are stored in the `collections` folder, with each collection having a subfolder.
This site uses the following collections:

- Opportunities (`collections/_opportunities`)
- Resources (`collections/_resources`)

(Please ignore other folders inside `collections`: they are there to prepare for future site expansion)

## How to update or add people

"People" is _not_ a collection.
Instead, all the information about people is stored as "data", in YAML files that live in the `_data` folder. This is easier to manage than if each person had a separate Markdown file, since there are many people.

Information about **Steering Committee** members is stored in `steering.yml`.
There are instructions at the top of the file explaining how to create a new entry.
People will be displayed on the site in the order in which they appear in this file, so if you are adding new people try to put them in the right spot (alphabetical by family name).

Information about **participants** in specific events is stored in a separate YAML file, such as `participants_2024.yml`.
It's usually easiest to compile long lists like these using a spreadsheet, and then convert from CSV to YAML. The command line tool [`yq`](https://mikefarah.gitbook.io/yq) can convert a CSV file into YAML in one line:

```bash
yq -p=csv data.csv > data.yml
```

(`yq` can also help [reshape the YAML file](https://mikefarah.gitbook.io/yq/recipes) if the initial conversion isn't what you had in mind)
