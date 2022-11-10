---
layout: default
css: [assets/css/markdown.css]
js: [assets/js/menu.js]
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
<footer>
    {% include main_menu.md %}
    <aside>
        If you find any mistakes in these materials or have any suggestions then please report them to the module leader.
    </aside>
    <small>&copy; Dr Graeme Stuart</small>
</footer>