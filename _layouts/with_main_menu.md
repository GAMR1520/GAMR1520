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
    {% include main_menu.md id="menu" %}
</header>
<main>
{{ content }}
</main>