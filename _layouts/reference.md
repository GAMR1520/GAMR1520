---
layout: index
---

{% if page.lang == "python" %}
{% include python_header.md %}
{% elsif page.lang == "js" %}
{% include js_header.md %}
{% endif %}

<h2>{{page.title}}</h2>
{% if page.week %}
{% assign week = site.weeks | where:"week", page.week | first %}
<small>
    Part of 
    <a href="{{week.url | relative_url }}">Week {{week.week}}: {{week.title}}</a>
</small>
{% endif %}
{{ content }}
