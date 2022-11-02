<nav id="menu">
    <a href="{{ "/labs" | relative_url }}">Labs</a>
    <nav>
    {% for page in site.python %}
        <a href="{{ page.url }}">{{ page.title }}</a>
    {% endfor %}
    </nav>
</nav>
