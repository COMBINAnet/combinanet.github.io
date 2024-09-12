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

  <div class="row row-cols-1 row-cols-md-2 justify-content-center py-3">
  {% for person in site.data.steering %}
    {% include people_horizontal.liquid %}
  {% endfor %}
  </div>
</section>

{% if site.data.participants_2024 %}
---

<section class="participants">
  <h2 id="participants-2024">2024 Workshop Participants</h2>
  <p>Dates, location, theme of 2024 workshop</p>

  <figure>
  <img src="/assets/img/workshop_2024.jpg" width="100%" height="auto">
  <figcaption>Participants at the 2024 COMBINA workshop, in Panamá. Photo: </figcaption>
  </figure>
  
  <dl class="container-grid">
    {% for person in site.data.participants_2024 %}
    <div class="card border-light" id="{{ person.name | slugify: "latin" }}">
      <dt class="px-2 pt-2">{{person.name}}{% if person.degrees %}, {{person.degrees}} {% endif %}</dt>
      <dd class="px-2 pb-2 text-muted">{{person.affiliation}}</dd>
      <dd class="card-footer d-flex justify-content-between align-items-center pl-2 pr-3 py-1 ">
          {% if person.country %}
            {% assign country_data = site.data.country | where: 'code', person.country | first %}
            <figure class="country text-muted">
              <img
                src="/assets/img/flags/{{- country_data.code -}}.svg"
                width="30"
                alt=""
              >
              <figcaption class="ml-2">{{- country_data.name -}}</figcaption>
            </figure>
          {% endif %}
          <div>{% include social_people.liquid class="card-link" %}</div>
        </dd>
    </div>
    {% endfor %}
  </dl>
</section>
{% endif %}