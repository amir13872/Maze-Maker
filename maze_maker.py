import random

def create_maze(width, height):
    """
    Generates a random maze using recursive backtracking.
    
    Args:
        width (int): Width of the maze.
        height (int): Height of the maze.

    Returns:
        list: A 2D grid representing the maze, where 1 is a wall and 0 is a path.
    """
    # Initialize the grid with walls
    WALL = 1
    PATH = 0
    grid = [[WALL for _ in range(width)] for _ in range(height)]

    # Start at a random cell
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[start_y][start_x] = PATH

    # Possible directions: up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def backtrack(x, y):
        """
        Recursively carves out paths in the maze using backtracking.

        Args:
            x (int): Current x-coordinate.
            y (int): Current y-coordinate.
        """
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == WALL:
                # Carve the path
                grid[ny - dy][nx - dx] = PATH
                grid[ny][nx] = PATH
                backtrack(nx, ny)

    # Start the maze generation
    backtrack(start_x, start_y)

    return grid

# Example usage
if __name__ == "__main__":
    maze = create_maze(42, 22)
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))
