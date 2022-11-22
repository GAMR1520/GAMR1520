def formatted_list(items, title="list", border='*', padding=2):
    width = max([len(i) for i in items + [title]]) + padding * 2
    hline = border * width
    result = [hline, title, hline] + items + [hline]
    result = [f"{border}{i.center(width)}{border}" for i in result]
    return "\n".join(result)

items = ["apples", "bananas", "cherries"]
print(formatted_list(items, title="fruit", border="+", padding=10))