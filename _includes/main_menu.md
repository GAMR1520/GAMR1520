<nav{% if include.id %} id="{{include.id}}"{% endif %}>
{% for item in site.data.navigation %}
    <a href="{{ item.link | relative_url }}"
        {% if page.url == item.link %}class="current"{% endif %}
    >{{ item.name }}</a>
{% endfor %}

{% for week in site.weeks %}
    <a href="{{week.url}}"
        {% if page.url == item.link %}class="current"{% endif %}
    >Week {{week.week}}</a>
{% endfor %}
</nav>

