def formatted_list(items, title="list", ch='*', pad=4):
    width = max([len(i) for i in items + [title]]) + pad
    hline = ch * width
    result = [hline, title, hline] + items + [hline]
    result = [f"{ch}{i.center(width)}{ch}" for i in result]
    return "\n".join(result)

f = ['apples', 'bananas', 'cherries']
print(formatted_list(f, title='fruit', ch="+", pad=20))
