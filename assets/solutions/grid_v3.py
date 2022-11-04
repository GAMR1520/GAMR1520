grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
} # The game is already won!

grid[(1, 0)] = "O"  # Forced move
grid[(2, 2)] = "X"  # The clincher
grid[(0, 0)] = "O"  # Forced move
grid[(0, 2)] = "X"  # X wins!

# fill in the grid with spaces
for y in range(3):
    for x in range(3):
        if (x, y) not in grid:
            grid[(x, y)] = " "

# print it out, line-by-line
print("\n--- --- ---\n".join(["|".join([f" {grid[(x, y)]} " for x in range(3)]) for y in range(3)]))