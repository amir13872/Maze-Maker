import random

def create_maze(width, height):
    # Initialize the grid with walls
    grid = [[1 for _ in range(width)] for _ in range(height)]

    # Start at a random cell
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[start_y][start_x] = 0

    # Recursive backtracking function
    def backtrack(x, y):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if (0 <= nx < width) and (0 <= ny < height) and grid[ny][nx] == 1:
                grid[ny - dy][nx - dx] = 0
                grid[ny][nx] = 0
                backtrack(nx, ny)

    backtrack(start_x, start_y)

    return grid

# Example usage
maze = create_maze(42, 22)

# Add a border around the maze
border_maze = [['#' for _ in range(52)] for _ in range(52)]
for i in range(50):
    for j in range(50):
        border_maze[i + 1][j + 1] = '#' if maze[i][j] else ' '

# Print the maze with a border
for row in border_maze:
    print(''.join(row))
