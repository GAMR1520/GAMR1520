---
layout: default
---
<header>
    {% include main_title.md %}
    <button id="menuToggler">
        <span></span>
        <span></span>
        <span></span>
    </button>
    {% include main_menu.md id="menu" %}
</header>
<main>
{{ content }}
</main>