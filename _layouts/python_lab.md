---
layout: default
---

<header>
    <a href="/">
        <img src="{{ site.baseurl }}/img/python-logo-only.svg" class="logo" alt="python logo">
        {% include main_title.html %}
        <img src="{{ site.baseurl }}/img/js-logo.svg" class="logo" alt="python logo">
    </a>
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
<footer>&copy; Dr Graeme Stuart</footer>