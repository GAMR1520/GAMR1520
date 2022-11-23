<nav{% if include.id %} id="{{include.id}}"{% endif %}>
{% for item in site.pages %}
    {% if item.menu %}
    <a href="{{ item.url | relative_url }}"
        {% if page.url == item.url %}class="current"{% endif %}
    >{{ item.menu }}</a>
    {% endif %}
{% endfor %}

{% for week in site.weeks %}
    {% if week.status == "draft" %}{% continue %}{% endif %}
    <a href="{{week.url | relative_url }}" {% if page.url == week.url %}class="current"{% endif %}>
        Week {{week.week}}{% if week.status == "draft" %} (draft){% endif %}
    </a>
{% endfor %}
</nav>

