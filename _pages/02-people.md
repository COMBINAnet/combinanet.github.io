---
layout: page
title: People
permalink: /people/
description: Our network of collaborators
nav: true
nav_order: 2
classes: layout--people
---

<section class="steering">
  <h2 id="steering">Steering Committee</h2>
  <p>A brief description of the role of the steering committee.</p>

  <div class="row justify-content-center py-3">
  {% for person in site.data.steering %}
    {% include people_horizontal.liquid %}
  {% endfor %}
  </div>
</section>

{% if site.data.collaborators %}
---

<section class="network">
<h2 id="network">Network</h2>
<p>A brief description of how COMBINA affiliates join and participate in the network.</p>

  {% for collaborator in site.data.collaborators %}
  <div id = "{{ collaborator.name | replace: ' ', '-' | remove: '.' }}" class="row" style="padding-top: 60px; margin-top: -60px; padding-bottom: 20px;">
  <strong>{{collaborator.name}}{% if collaborator.degrees %}, {{collaborator.degrees}} {% endif %}</strong><br>  
    {{collaborator.affiliation}}<br>
    {% if collaborator.website %} <i class="fa fa-globe"></i> <a href= "{{collaborator.website}}" target="_blank">{{collaborator.website}}</a>  {% endif %}
  </div>
  {% endfor %}

</section>
{% endif %}