---
layout: page
title: Contact
permalink: /contact/
description:
nav: true
nav_order: 7
classes: layout--contact
---

Para obtener más información sobre COMBINA o conectarse con nuestra red en crecimiento, ¡comuníquese!

To learn more about COMBINA or get connected to our growing network, please reach out!

<div class="alert alert-primary text-center">
  <dl>
    <dt>COMBINA Network Coordinator &bull; Coordinadora de la red COMBINA</dt>
    <dd>
      {% assign coordinator = site.data.steering | find: "role", "Network Coordinator" %}
      {{ coordinator.name }}, {{ coordinator.affiliation }}
    </dd>
    <dd><a class="alert-link" href="mailto:{{ site.email | encode_email }}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {{ site.email }}</a></dd>
  </dl>
</div>
