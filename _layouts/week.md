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

</section>

{% assign lectures = site.lectures | where:"week", page.week | sort: "lecture" %}

{% for lec in lectures %}

<section>

<h3><a href="{{lec.url | relative_url }}">Lecture {{lec.week}}.{{lec.lecture}}: {{lec.title}}</a></h3>

<p>{{lec.description}}</p>

</section>

{% endfor %}



{% assign exercises = site.exercises | where:"week", page.week | sort: "lab" %}

{% for ex in exercises %}

<section>

<h3><a href="{{ex.url | relative_url }}">Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}</a></h3>

<p>{{ex.description}}</p>

</section>

{% endfor %}

