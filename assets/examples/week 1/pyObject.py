import html
import sys

def attr(**attributes):
    return " ".join([f'{k.strip("_")}="{v}"' for k, v in attributes.items()]) or None

def tag(tag, content=None, **attributes):
    a = attr(**attributes)
    open_tag = " ".join([tag, a]) if a else tag
    if content:
        return f'<{open_tag}>{content}</{tag}>'
    return f'<{open_tag}>'


# we remove two from the reference count
# one due to our function argument, arg
# and one for the similar impact of getrefcount
def py_object(arg):
    refs = sys.getrefcount(arg) - 2 
    return {
        'id': f'{id(arg):#x}',
        'type': type(arg),
        'value': arg,
        'refs': refs
    }


def to_table(arg):
    data = py_object(arg)
    rows = [tag('th', "pyObject", colspan=2)]
    for key, value in data.items():
        th = tag('th', key)
        td = tag('td', html.escape(str(value)))
        rows.append(f'{th}{td}')
    result = "\n    ".join([tag('tr', row) for row in rows])
    return f"<table>\n    {result}\n</table>"

def to_svg(variable, arg):
    data = py_object(arg)
    v = tag('rect', width=200, height=100)
    return tag("svg", f"{v}", _class="pyObject", viewport="0 0 500 500")


# print(to_table(1))
print(attr())
print(attr(a=1))
print(to_table(1))
print(to_svg('a', 1))