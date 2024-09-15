---
layout: page
title: People
permalink: /people/
description: An international network connecting scientists, resource managers, and policy-makers
nav: true
nav_order: 2
classes: layout--people

sections:
  steering:
    title: Steering Committee
    data: steering.yml

  participants_2024:
    title: 2024 Workshop Participants
    description: |-
      COMBINA was officially launched at a [four day workshop](https://stri.si.edu/story/combina) held in Panama City in March, 2024. More than 70 participants from 12 countries attended.

      <figure>
      <img src="/assets/img/workshop_2024.jpg" width="100%" height="auto">
      <figcaption>Participants at the 2024 COMBINA workshop, in Panama City. Photo: Jorge Aleman.</figcaption>
      </figure>
    data: participants_2024.yml
---

{% include people_major.liquid data=page.sections.steering.data section="steering" title=page.sections.steering.title %}

---

{% include people_minor.liquid data=page.sections.participants_2024.data section="participants" title=page.sections.participants_2024.title description=page.sections.participants_2024.description %}
