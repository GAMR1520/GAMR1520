---
layout: index
---

{% if page.lang == "python" %}
    {% include python_header.md %}
{% endif %}

{% if page.lang == "js" %}
    {% include js_header.md %}
{% endif %}

{% if page.status == "draft" %}
<blockquote>
    <p>
        This is currently <strong>draft</strong> content, it may be incomplete or wrong.
    </p>
</blockquote>
{% endif %}


<section>
    <h2 class="{{page.lang}}"> Week {{page.week}}: {{page.title}}</h2>
    <small>
        Back to <a href="{{"/" | relative_url }}">home</a>
    </small>
    {{ content }}
</section>

{% assign lectures = site.lectures | where:"week", page.week | sort: "lecture" %}
{% if lectures.size > 0 %}
<section>
    <h2 class="{{page.lang}}">Lectures</h2>
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
{% endif %}

{% assign exercises = site.exercises | where:"week", page.week | sort: "lab" %}
{% if exercises.size > 0 %}
<section>
    <h2 class="{{page.lang}}">Lab exercises</h2>
    {% for ex in exercises %}
    <article>
        <h3><a href="{{ex.url | relative_url }}">Lab {{ex.week}}.{{ex.lab}}: {{ex.title}}</a></h3>
        <p>{{ex.description}}</p>
    </article>
    {% endfor %}
</section>
{% endif %}

{% assign references = site.references | where:"week", page.week %}
{% if references.size > 0 %}
<section>
    <h2 class="{{page.lang}}">Other resources</h2>
    <ul>
    {% for ref in references %}
        <li><a href="{{ref.url | relative_url }}">{{ref.title}}</a></li>
    {% endfor %}
    </ul>
</section>
{% endif %}