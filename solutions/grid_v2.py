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
        key = (x, y)
        if key not in grid:
            grid[key] = " "

# print it out, line-by-line
for y in range(3):
    print(" ".join([grid[(x, y)] for x in range(3)]))
        
