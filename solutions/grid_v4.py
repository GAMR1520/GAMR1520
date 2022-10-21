grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
} # The game is already won!

grid[(1, 0)] = "O"  # Forced move
grid[(2, 2)] = "X"  # The clincher
grid[(0, 0)] = "O"  # Forced move
grid[(0, 2)] = "X"  # X wins!

# A function to generate cell output
def cell(x, y):
    return " " if (x, y) not in grid else grid[(x, y)]

# Another function for a full row
def row(y):
    return "|".join([f" {cell(x, y)} " for x in range(3)])

# print it out, line-by-line
print()
print("\n--- --- ---\n".join([row(y) for y in range(3)]))
print()