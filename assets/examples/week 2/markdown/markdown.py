def html_element(content, tag, **attr):
    attrs = [f'{k.lstrip("_")}="{v}"' for k, v in attr.items()]
    attrs = " ".join(attrs)
    if attrs:
        attrs = f" {attrs}"
    return f"<{tag}{attrs}>{content}</{tag}>"

def parse_md_file(path):
    with path.open('r') as f:
        return f.read().split('\n\n')

def format_md_chunk(chunk):
    tag = "p"
    if chunk.startswith('# '):
        chunk = chunk[2:]
        tag = "h1"
    return html_element(chunk, tag)

def format_md_chunks(data):
    return [format_md_chunk(chunk) for chunk in data]

def convert(path):
    data = parse_md_file(path)
    data = format_md_chunks(data)
    return '\n\n'.join(data)