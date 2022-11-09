---
layout: default
---

<header>
    {% include main_title.md %}
    <button id="menuToggler">
        <div></div>
        <div></div>
        <div></div>
    </button>
    {% include main_menu.md id="menu" %}
</header>
<main>
    {% assign week = site.weeks | where:"week", page.week | first %}
    {% include python_header.md %}
    <h2>Lab {{page.week}}.{{page.lab}}: {{page.title}}</h2>
    <small>
    Part of <a href="{{week.url | relative_url }}">week {{week.week}}: {{week.title}}</a>
    </small>
    {{ content }}
</main>