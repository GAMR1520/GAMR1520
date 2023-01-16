---
layout: index
---

{% assign week = site.weeks | where:"week", page.week | first %}

{% if page.lang == "python" %}
{% include python_header.md %}
{% endif %}

{% if page.lang == "js" %}
{% include js_header.md %}
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

<h3>General setup</h3>
<p>
    For all lab exercises you should create a folder for the lab somewhere sensible.
</p>
<p>
    Assuming you have a <em>GAMR1520-labs</em> folder, you should create a <em>GAMR1520-labs/week_{{page.week}}</em> folder for this week and a <em>GAMR1520-labs/week_{{page.week}}/lab_{{page.week}}.{{page.lab}}</em> folder inside that.
</p>

{% if page.lang == "python" %}
<p>
    Create a collection of scripts.
    If necessary, use folders to group related examples. 
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
{% endif %}

{% if page.lang == "js" %}
<h3>JavaScript setup</h3>
<p>
    Though it is possible to contain everything within one file, a JavaScript project will usually contain a collection of multiple files.
</p>

<pre><code class="hljs language-markdown">GAMR1520-labs
└─ week_{{page.week}}
    └─ lab_{{page.week}}.{{page.lab}}
        ├─ experiment1
        │    ├─ index.html
        │    └─ scripts.js
        └─ experiment2
             ├─ index.html
             └─ scripts.js
</code></pre>
<p>
    For simple projects, there will always be an <em>index.html</em> and the javascript file can always be something like <em>scripts.js</em>, though you can choose your own names.
    Using the same template for multiple examples is convenient.
    Try to name your folders better than this, the folder name should reflect their content.
    For example, <em>blank_template</em>, <em>edit_elements</em> or <em>simple_drawing</em>.
</p>
<h3>Resources</h3>
<p>
    If you want to find out more information about any aspect of web development, the best resource is the 
    <a href="https://developer.mozilla.org/en-US/">Mozilla Developer Network</a>
    web documents, in particular 
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference">the JavaScript documentation</a> will be invaluable for this module.
</p>

{% endif %}
<h3>General approach</h3>
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
