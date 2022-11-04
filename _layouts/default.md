<!DOCTYPE html>
<html lang="en">
<head>
<title>{{ page.title }}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta property="og:title" content="{{ page.title }}">
<meta property="og:type" content="website" />
<meta property="og:description" content="GAMR1520 Markup Languages and Scripting" />
<meta name="author" content="Graeme Stuart">

<link rel="apple-touch-icon" sizes="180x180" href="{{ "/assets/favicon/apple-touch-icon.png" | relative_url }}">
<link rel="icon" type="image/png" sizes="32x32" href="{{ "/assets/favicon/favicon-32x32.png" | relative_url }}">
<link rel="icon" type="image/png" sizes="16x16" href="{{ "/assets/favicon/favicon-16x16.png" | relative_url }}">
<link rel="manifest" href="{{ "/assets/favicon/site.webmanifest" | relative_url }}">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/atom-one-dark-reasonable.min.css" integrity="sha512-RwXJS3k4Z0IK6TGoL3pgQlA9g2THFhKL7z9TYWdAI8u6xK0AUuMWieJuWgTRayywC9A94ifUj1RzjDa1NIlUIg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<link rel="stylesheet" href="{{ "/assets/css/markdown.css" | relative_url }}" type="text/css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js" integrity="sha512-gU7kztaQEl7SHJyraPfZLQCNnrKdaQi5ndOyt4L4UPL/FHDd/uB9Je6KDARIqwnNNE27hnqoWLBq+Kpe4iHfeQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>hljs.highlightAll();</script>
<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>
</head>

<body>
    {{ content }}
    <footer>
        {% include main_menu.md %}
        <aside>
            If you find any mistakes in these materials or have any suggestions then please report them to the module leader.
        </aside>
        <small>&copy; Dr Graeme Stuart</small>
    </footer>
    <script src="{{ "/assets/js/menu.js" | relative_url }}"></script>
</body>
</html>