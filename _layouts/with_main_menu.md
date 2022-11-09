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
{{ content }}
</main>