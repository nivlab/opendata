---
layout: default
title: Home
nav_order: 1
permalink: /
last_modified_date: 2020-08-06
---

# OpenData

{% for dataset in site.datasets %}
  <p>{{ dataset.year }}</p>
  <p>{{ dataset.permalink }}</p>
{% endfor %}
