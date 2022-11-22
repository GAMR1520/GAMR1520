from pathlib import Path
import markdown

inpath = Path(__file__).parent / 'test.md'
outpath = Path(__file__).parent / 'test.html'

with outpath.open('w') as f:
    html = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Markdown converted output</title>
    </head>
    <body>
{markdown.convert(inpath)}
    </body>
    </html>
    """
    f.write(html)
