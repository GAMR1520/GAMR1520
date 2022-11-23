---
layout: index
menu: Home
title: Welcome to GAMR1520!
---

{% include combined_header.md %}

This module covers the dynamically typed languages *python* and *javascript*.

The module materials are organised as a series of interlinked web pages containing lecture slides, introductory materials, example code and exercises which you should attempt.
You will find the same pages are linked multiple times, often as reminders of the basic concepts.
Please read each page at least once and use your judgement as to whether you need to review concepts or can skip over them when they are linked again.


{% for week in site.weeks %}


{% if week.status == "draft" %}
{% break %}

<blockquote>
    <p>
        This is currently <strong>draft</strong> content, it may be incomplete or wrong.
    </p>
</blockquote>
{% endif %}

## [Week {{week.week}}: {{week.title}}]({{week.url | relative_url }})
{: .{{week.lang}}}
{{ week.content | markdownify }}
### Lectures
{% assign lectures = site.lectures | where:"week", week.week | sort: "lecture" %}
{% for lec in lectures %}
 - [Lecture {{lec.week}}.{{lec.lecture}}: {{lec.title}}]({{lec.url | relative_url }}){% endfor %}

### Exercises
{% assign exercises = site.exercises | where:"week", week.week | sort: "lab" %}
{% for ex in exercises %}
 - [Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}]({{ex.url | relative_url }}){% endfor %}
{% endfor %}<!-- end of week -->

