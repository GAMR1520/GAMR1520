---
layout: index
title: Welcome to GAMR1520!
---

This module covers the dynamically typed languages *python* and *javascript*.

{% include combined_header.md %}

## Lab exercises

> **Be scientific**
>
> As you work through these exercises, make sure you experiment.
> *Write your own code and predict what will happen*. 
> Be inquisitive, and see if your instincts are correct.
> If something unexpected happens, this is good.
> It's time to stop and think.

> **Don't let it go**
>
> The material is just a guide, your task is to become a good python programmer.
> If you're not sure, *ask the obvious questions*.
> Ask your colleagues or tutor as necessary.
>
> If you understand the material, try to come up with really hard questions.
> *We don't know everything*, if we don't know the answer, we can learn together.


{% for week in site.weeks %}


### [Week {{week.week}}: {{week.title}}]({{week.url | relative_url }})

{{ week.content | markdownify }}


{% assign exercises = site.exercises | where:"week", week.week | sort: "lab" %}

{% for ex in exercises %}
- [Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}]("{{ex.url | relative_url }}"){% endfor %}


{% endfor %}<!-- end of week -->
