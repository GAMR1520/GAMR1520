<nav id="menu">
    <a href="{{ site.baseurl }}/labs">Labs</a>
    <nav>
    {% for page in site.python %}
        <a href="{{ page.url }}">{{ page.title }}</a>
    {% endfor %}
    </nav>
</nav>
