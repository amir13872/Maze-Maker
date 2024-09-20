# Maze-Maker

Maze-Maker is a Python script that generates random mazes using a recursive backtracking algorithm. The maze is represented as a 2D grid where walls are denoted by `1` and paths by `0`.

## Features
- Generates mazes with customizable width and height.
- Uses recursive backtracking to carve out paths.
- Displays the maze in the console with `#` as walls and spaces as paths.

## How It Works
1. The grid is initialized with walls.
2. A random starting point is selected.
3. The recursive backtracking algorithm is applied to carve out paths in the maze.
4. Directions (up, down, left, right) are randomly shuffled and processed.

## Example Usage

To generate a 42x22 maze, run the following command:

```bash
python maze_maker.py
```

## Customization

To customize the size of the maze, modify the width and height in the create_maze function:

```
maze = create_maze(50, 30)  # Generates a 50x30 maze
```

## Requirements

Python 3.x

## Contribution

Contributions are welcome! If you'd like to contribute to Maze-Maker, follow these steps:

1.  Fork the repository.
2.  Create a new branch: `git checkout -b my-feature`.
3.  Make your changes and commit them: `git commit -m 'Add my feature'`.
4.  Push to the branch: `git push origin my-feature`.
5.  Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Amir Mahdi Zare

```
mahnaznamani007@gmail.com
```
