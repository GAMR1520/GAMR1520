---
layout: index
---

{% assign week = site.weeks | where:"week", page.week | first %}

{% if page.lang == "python" %}
{% include python_header.md %}
{% endif %}

{% if week.status == "draft" %}
<blockquote>
    <p>
        This is currently <strong>draft</strong> content, it may be incomplete or wrong.
    </p>
</blockquote>
{% endif %}

<h2>Lab {{page.week}}.{{page.lab}}: {{page.title}}</h2>

<small>
    Part of 
    <a href="{{week.url | relative_url }}">Week {{week.week}}: {{week.title}}</a>
</small>

{{ content }}
