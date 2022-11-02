---
layout: default
---

<header>
    {% include main_title.md %}
    <div id="menuToggler">
        <div></div>
        <div></div>
        <div></div>
    </div>
    {% include lab_menu.md %}
</header>
<main>
    {% include python_header.md %}
    <h2>{{page.title}}</h2>
    {{ content }}
</main>
