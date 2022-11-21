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

<blockquote>
<p>
    For all lab exercises you should create a folder for the lab somewhere sensible.
</p>
<p>
    Assuming you have a <em>GAMR1520-labs</em> folder, you should create a <em>GAMR1520-labs/week_{{page.week}}</em> folder for this week and a <em>GAMR1520-labs/week_{{page.week}}/lab_{{page.week}}.{{page.lab}}</em> folder inside that.
</p>
<pre>GAMR1520-labs
└─ week_{{page.week}}
    └─ lab_{{page.week}}.{{page.lab}}
        ├─ experiment1.py
        └─ experiment2.py
</pre>
<p>
    Try to name your files better than this, the filename should reflect their content.
</p>
</blockquote>

{{ content }}
