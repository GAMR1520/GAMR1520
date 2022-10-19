grid = {
    (1, 1): "X",
    (0, 1): "O",
    (1, 2): "X",
} # The game is already won!

grid[(1, 0)] = "O"  # Forced move
grid[(2, 2)] = "X"  # The clincher
grid[(0, 0)] = "O"  # Forced move
grid[(0, 2)] = "X"  # X wins!

output = ""
if (0, 0) in grid:
    output += grid[(0, 0)]
else:
    output += " "

if (1, 0) in grid:
    output += grid[(1, 0)]
else:
    output += " "

if (2, 0) in grid:
    output += grid[(2, 0)]
else:
    output += " "

output += "\n"

if (0, 1) in grid:
    output += grid[(0, 1)]
else:
    output += " "

if (1, 1) in grid:
    output += grid[(1, 1)]
else:
    output += " "

if (2, 1) in grid:
    output += grid[(2, 1)]
else:
    output += " "

output += "\n"

if (0, 2) in grid:
    output += grid[(0, 2)]
else:
    output += " "

if (1, 2) in grid:
    output += grid[(1, 2)]
else:
    output += " "

if (2, 2) in grid:
    output += grid[(2, 2)]
else:
    output += " "

print(output)