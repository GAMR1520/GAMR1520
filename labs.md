---
layout: index
title: Lab materials
---

The lab materials are organised as a series of interlinked web pages containing introductory materials, example code and exercises which you should attempt.
You will find the same pages are linked multiple times, often as reminders of the basic concepts.
Please read each page at least once and use your judgement as to whether you need to review concepts or can skip over them when they are linked again.







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

## Week {{week.week}}: {{week.title}}

{{ week.content | markdownify }}

{% assign exercises = site.exercises | where:"week", week.week | sort: "lab" %}

{% for ex in exercises %}

### [Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}]({{ex.url}})

{{ex.description}}

{% endfor %}

{% endfor %}

