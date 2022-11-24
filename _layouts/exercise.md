---
layout: index
---

{% assign week = site.weeks | where:"week", page.week | first %}

{% if page.lang == "python" %}
{% include python_header.md %}
{% endif %}

{% if week.status == "draft" %}
<blockquote>
    <p>
        This is currently <strong>draft</strong> content, it may be incomplete or wrong.
    </p>
</blockquote>
{% endif %}

<h2 class="{{page.lang}}">Lab {{page.week}}.{{page.lab}}: {{page.title}}</h2>


<small>
    Part of 
    <a href="{{week.url | relative_url }}">Week {{week.week}}: {{week.title}}</a>
</small>

<blockquote>
<p>
    For all lab exercises you should create a folder for the lab somewhere sensible.
</p>
<p>
    Assuming you have a <em>GAMR1520-labs</em> folder, you should create a <em>GAMR1520-labs/week_{{page.week}}</em> folder for this week and a <em>GAMR1520-labs/week_{{page.week}}/lab_{{page.week}}.{{page.lab}}</em> folder inside that.
</p>
<pre><code class="hljs language-markdown">GAMR1520-labs
└─ week_{{page.week}}
    └─ lab_{{page.week}}.{{page.lab}}
        ├─ experiment1.py
        └─ experiment2.py
</code></pre>
<p>
    Try to name your files better than this, the filename should reflect their content.
    For example, <em>string_methods_.py</em>, <em>conditionals.py</em> or <em>while_loops.py</em>.
</p>
<p> 
    Make sure your filenames give clues about what is inside each file.
    A future version of you will be looking back at these, trying to remember where a particular example was.
</p>
<p>
    As you encounter new concepts, try to create examples for yourself that prove you understand what is going on.
    <em>Try to break stuff</em>, its a good way to learn.
    But <strong>always save a working version</strong>.
</p>
<p>
    Modifying the example code is a good start, but try to write your own programmes from scratch, based on the example code.
    They might start very simple, but over the weeks you can develop them into more complex programmes.
</p>
<p>
    Think of a programme you would like to write (don't be too ambitious).
    Break the problem down into small pieces and spend some time each session trying to solve a small problem.
</p>
</blockquote>

{{ content }}
