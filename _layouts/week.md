---
layout: index
---

{% if page.lang == "python" %}
    {% include python_header.md %}
{% endif %}

{% if page.lang == "js" %}
    {% include js_header.md %}
{% endif %}

<section>
    <h2 class="{{page.lang}}"> Week {{page.week}}: {{page.title}}</h2>
    <small>
        Back to <a href="{{"/" | relative_url }}">home</a>
    </small>
    {{ content }}
</section>

<section>
    <h2 class="{{page.lang}}">Lectures</h2>
    {% assign lectures = site.lectures | where:"week", page.week | sort: "lecture" %}
    {% for lec in lectures %}
    <article>
        <h3>
            <a href="{{lec.url | relative_url }}">
                Lecture {{lec.week}}.{{lec.lecture}}: {{lec.title}}
            </a>
        </h3>
        <p>{{lec.description}}</p>
    </article>
    {% endfor %}
</section>

<section>
    <h2 class="{{page.lang}}">Lab exercises</h2>
    {% assign exercises = site.exercises | where:"week", page.week | sort: "lab" %}
    {% for ex in exercises %}
    <article>
        <h3><a href="{{ex.url | relative_url }}">Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}</a></h3>
        <p>{{ex.description}}</p>
    </article>
    {% endfor %}
</section>

<section>
    <h2 class="{{page.lang}}">Other resources</h2>
    {% assign references = site.references | where:"week", page.week %}
    <ul>
    {% for ref in references %}
        <li><a href="{{ref.url | relative_url }}">{{ref.title}}</a></li>
    {% endfor %}
    </ul>
</section>
