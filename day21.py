grid = [[char for char in line.strip()] for line in open("inputs/test21").readlines()]


def print_grid(grid):
    for row in grid:
        print(''.join(row))


# Function to find the position of 'S'
def find_s(grid):
    return next(((i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == 'S'), None)


def find_middle(grid):
    rows = len(grid)
    cols = len(grid[0])

    mid_row = rows // 2 if rows % 2 != 0 else rows // 2 - 1
    mid_col = cols // 2 if cols % 2 != 0 else cols // 2 - 1

    return mid_row, mid_col


def extend_grid_replace_s(grid, steps):
    rows = len(grid)
    cols = len(grid[0])

    middle = find_s(grid)
    grid[middle[0]][middle[1]] = '.'  # Replace 'S' with '.' in the original grid


    # Create an extended grid with the appropriate size
    extended_rows = rows * (2 * steps + 1)
    extended_cols = cols * (2 * steps + 1)
    extended_grid = [['.' for _ in range(extended_cols)] for _ in range(extended_rows)]

    # Copy the original grid into the center of the extended grid
    for i in range(rows):
        for j in range(cols):
            extended_grid[i + rows * steps][j + cols * steps] = grid[i][j]

    # Copy the original grid to all sides
    for i in range(rows):
        for j in range(cols):
            # Copy to the top side
            for k in range(steps):
                extended_grid[i + k * rows][j + cols * steps] = grid[i][j]
            # Copy to the bottom side
            for k in range(1, steps + 1):
                extended_grid[i + k * rows + rows * steps][j + cols * steps] = grid[i][j]

    for i in range(extended_rows):
        for j in range(cols):
            # Copy to the left side
            for k in range(steps):
                extended_grid[i][j + k * cols] = extended_grid[i][j + cols * steps]
            # Copy to the right side
            for k in range(1, steps + 1):
                extended_grid[i][j + k * cols + cols * steps] = extended_grid[i][j + cols * steps]

    middle = find_middle(extended_grid)
    extended_grid[middle[0]][middle[1]] = 'S'

    return extended_grid


def navigate(grid, steps):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    positions = {find_s(grid)}

    def is_valid_position(pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == '.'

    for step in range(steps):
        #print(step)
        for cur_position in positions:
            grid[cur_position[0]][cur_position[1]] = '.'

        positions = {(pos[0] + move[0], pos[1] + move[1]) for pos in positions for move in moves if is_valid_position((pos[0] + move[0], pos[1] + move[1]))}
        for cur_position in positions:
            grid[cur_position[0]][cur_position[1]] = 'O'
        #print_grid(grid)

    return sum(row.count('O') for row in grid)


#print(navigate(grid, 1000))

print_grid(grid)
new = extend_grid_replace_s(grid, 100)

print(navigate(new, 500))
#print_grid(new)
