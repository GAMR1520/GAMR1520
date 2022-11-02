<nav{% if include.id %} id="{{include.id}}"{% endif %}>
{% for item in site.data.navigation %}
    <a href="{{ item.link | relative_url }}"
        {% if page.url == item.link %}class="current"{% endif %}
    >{{ item.name }}</a>
    {% for subitem in item.content %}
        <a href="{{ subitem.link | relative_url }}"
            {% if page.url == subitem.link %}class="current"{% endif %}
        >{{ subitem.name }}</a>
    {% endfor %}
{% endfor %}
</nav>

