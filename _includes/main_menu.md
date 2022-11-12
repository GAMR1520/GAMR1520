<nav{% if include.id %} id="{{include.id}}"{% endif %}>
{% for item in site.pages %}
    {% if item.menu %}
    <a href="{{ item.url | relative_url }}"
        {% if page.url == item.url %}class="current"{% endif %}
    >{{ item.menu }}</a>
    {% endif %}
{% endfor %}

{% for week in site.weeks %}
    <a href="{{week.url | relative_url }}"
        {% if page.url == week.url %}class="current"{% endif %}
    >Week {{week.week}}</a>
{% endfor %}
</nav>

