---
layout: index
title: Welcome to GAMR1520!
---

This module covers the dynamically typed languages *python* and *javascript*.

{% include combined_header.md %}


{% for week in site.weeks %}


## [Week {{week.week}}: {{week.title}}]({{week.url}})

{{ week.content | markdownify }}

{% endfor %}
