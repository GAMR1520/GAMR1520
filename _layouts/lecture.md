---
layout: default
css: [assets/css/lecture.css]
js: [assets/js/lecture.js, assets/js/menu.js]
---

<header>
    {% include main_title.md %}
    <button id="menuToggler">
        <span></span>
        <span></span>
        <span></span>
    </button>
    {% include main_menu.md id="menu" %}
</header>
<main class="{{page.lang}}">
    <section class="slide home">
        <section>
            <h2>GAMR1520</h2>
            <h3>Markup languages and scripting</h3>
            <h4>{{page.title}}</h4>
        </section>
        <p>
            <strong>Dr Graeme Stuart</strong><br>
        </p>
    </section>
    {{ content }}
    <section class="slide home">
        <div>
            <h3>Thanks for listening</h3>
            <h4>Any questions?</h4>
        </div>
        <p>
            <strong>Dr Graeme Stuart</strong><br>
        </p>
    </section>
</main>
<footer>
    <div class="controls">
        <button id="previousSlide" aria-label="previous slide">◄</button>
        <span id="slideNumber"></span>
        of
        <span id="slideCount"></span>
        <button id="nextSlide" aria-label="next slide">►</button>
    </div>
    <div class="fadeaway">
        You can swipe left and right
    </div>
    <small>&copy; Dr Graeme Stuart</small>
</footer>
