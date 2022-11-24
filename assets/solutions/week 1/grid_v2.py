grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
    (1, 0): "O",
    (2, 2): "X",
    (0, 0): "O",
    (0, 2): "X",
}

for y in range(3):
    for x in range(3):
        key = (x, y)
        print(grid.get(key, " "), end=" ")
    print()