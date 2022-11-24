grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
    (1, 0): "O",
    (2, 2): "X",
    (0, 0): "O",
    (0, 2): "X",
}

# Splitting the logic out into a function makes it longer, and a bit easier to read.


horizontal_line = "\n--- --- ---\n"
vertical_line = "|"

def format_cell(x, y):
    value = grid.get((x, y), ' ')
    return f" {value} "

def row(y):
    cells = [format_cell(x, y) for x in range(3)]
    return vertical_line.join(cells)

print()
print(horizontal_line.join([row(y) for y in range(3)]))
print()
