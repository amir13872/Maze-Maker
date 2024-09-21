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
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 1:
                grid[ny - dy][nx - dx] = 0
                grid[ny][nx] = 0
                backtrack(nx, ny)

    # Start the maze generation
    backtrack(start_x, start_y)
    return grid

def add_border_to_maze(maze):
    height, width = len(maze), len(maze[0])

    # Add a border with a 1-cell margin around the maze
    border_maze = [['*' for _ in range(width + 4)] for _ in range(height + 4)]
    for i in range(height):
        for j in range(width):
            border_maze[i + 2][j + 2] = ' ' if maze[i][j] == 0 else '#'

    # Add "Enter" and "Exit" labels
    border_maze[1][2:7] = list('Enter')
    border_maze[height + 3][width - 3:width + 1] = list('Exit')

    return border_maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Example usage
maze = create_maze(42, 22)
bordered_maze = add_border_to_maze(maze)
print_maze(bordered_maze)
