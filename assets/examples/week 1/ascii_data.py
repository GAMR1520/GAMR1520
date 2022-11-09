import string

data = string.ascii_lowercase
result = "".join([f"\t<span>{c} = {ord(c)}</span>\n" for c in data])
print(f'<div class="auto-grid">\n{result}</div>')