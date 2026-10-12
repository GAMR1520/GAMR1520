"""Functions implementing the core behaviour of the 2048 tile grid"""

def stack_left(row):
    """move the non-None items in one row to the left"""
    return sorted(row, key=lambda tile: tile is None)

def merge_left(stacked_row):
    """Merge similar non-None items to the left"""
    for i in range(3):
        if stacked_row[i] and stacked_row[i] == stacked_row[i+1]:
            stacked_row[i] *= 2
            stacked_row[i + 1] = None
    return stacked_row

def row_left(row):
    """A full move involves stacking, merging and then stacking again"""
    stacked = stack_left(row)
    merged = merge_left(stacked)
    return stack_left(merged)

def move_left(grid):
    """moving a full grid to the left by moving each row to the left"""
    return [row_left(row) for row in grid]

def reverse(grid):
    """flip the grid horizontally"""
    return [list(reversed(row)) for row in grid]

def move_right(grid):
    """move right by flipping the grid and moving left"""
    grid = reverse(grid)
    grid = move_left(grid)
    return reverse(grid)

def transpose(grid):
    """flip the grid diagonally"""
    return [list(col) for col in zip(*grid)]

def move_up(grid):
    """move up by transposing the grid and moving left"""
    grid = transpose(grid)
    grid = move_left(grid)
    return transpose(grid)

def move_down(grid):
    """move down by transposing the grid and moving right"""
    grid = transpose(grid)
    grid = move_right(grid)
    return transpose(grid)

def has_gaps(grid):
    for row in grid:
        if None in row:
            return True
    return False

def has_vertical_merges(data):
    for row in range(3):
        for col in range(4):
            if data[row][col] == data[row + 1][col]:
                return True
    return False

def has_horizontal_merges(data):
    for row in range(4):
        for col in range(3):
            if data[row][col] == data[row][col + 1]:
                return True
    return False


def is_game_over(data):
    return not (
        has_gaps(data) or 
        has_vertical_merges(data) or 
        has_horizontal_merges(data)
    )


def horizontal_points(data):
    data = [stack_left(row) for row in data]
    points = 0
    for row in range(4):
        for col in range(3):
            if data[row][col] and data[row][col] == data[row][col + 1]:
                points += data[row][col] * 2
                data[row][col] = None
                data[row][col + 1] = None
    return points

def vertical_points(grid):
    grid = transpose(grid)
    return horizontal_points(grid)
