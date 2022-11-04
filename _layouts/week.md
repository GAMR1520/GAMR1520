---
layout: with_main_menu
---

{% if page.lang == "python" %}
    {% include python_header.md %}
{% endif %}

{% if page.lang == "js" %}
    {% include js_header.md %}
{% endif %}

<section>
<h2> Week {{page.week}}: {{page.title}}</h2>
<small>
Back to <a href="{{"/" | relative_url }}">home</a>
</small>

{{ content }}

{% assign exercises = site.exercises | where:"week", page.week | sort: "lab" %}

{% for ex in exercises %}

<h3><a href="{{ex.url}}">Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}</a></h3>

<p>{{ex.description}}</p>

{% endfor %}

</section>
