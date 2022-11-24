grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
    (1, 0): "O",
    (2, 2): "X",
    (0, 0): "O",
    (0, 2): "X",
}

# A nested list comprehension is pretty hard to read
print("\n--- --- ---\n".join(["|".join([f" {grid.get((x, y), ' ')} " for x in range(3)]) for y in range(3)]))


