#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define WIDTH 42
#define HEIGHT 22

// Function to create a maze
int** createMaze() {
    // Initialize the grid with walls
    int** grid = (int**)malloc(HEIGHT * sizeof(int*));
    for (int i = 0; i < HEIGHT; i++) {
        grid[i] = (int*)malloc(WIDTH * sizeof(int));
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = 1;
        }
    }

    // Designate the entrance and exit
    int entranceX = 1;
    int entranceY = 1;
    int exitX = WIDTH - 2;
    int exitY = HEIGHT - 2;
    grid[entranceY][entranceX] = 0;
    grid[exitY][exitX] = 0;

    // Start at a random cell
    srand(time(NULL));
    int startX, startY;
    do {
        startX = rand() % WIDTH;
        startY = rand() % HEIGHT;
    } while ((startX == entranceX && startY == entranceY) || (startX == exitX && startY == exitY));
    grid[startY][startX] = 0;

    // Recursive backtracking function
    void backtrack(int x, int y) {
        int directions[4][2] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int i = 0; i < 4; i++) {
            int dirX = directions[i][0];
            int dirY = directions[i][1];
            int nx = x + 2 * dirX;
            int ny = y + 2 * dirY;
            if (nx >= 0 && nx < WIDTH && ny >= 0 && ny < HEIGHT && grid[ny][nx] == 1) {
                grid[ny - dirY][nx - dirX] = 0;
                grid[ny][nx] = 0;
                backtrack(nx, ny);
            }
        }
    }

    // Start the maze generation
    backtrack(startX, startY);

    return grid;
}

// Function to add a border to the maze
char** addBorderToMaze(int** maze) {
    int height = HEIGHT;
    int width = WIDTH;

    // Add a border with a 1-cell margin around the maze
    char** borderMaze = (char**)malloc((height + 4) * sizeof(char*));
    for (int i = 0; i < height + 4; i++) {
        borderMaze[i] = (char*)malloc((width + 4) * sizeof(char));
        for (int j = 0; j < width + 4; j++) {
            borderMaze[i][j] = '*';
        }
    }

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            borderMaze[i + 2][j + 2] = maze[i][j] == 0 ? ' ' : '#';
        }
    }

    // Add "Enter" and "Exit" labels
    char* enter = "Enter";
    char* exit = "Exit";
    for (int i = 0; i < strlen(enter); i++) {
        borderMaze[1][2 + i] = enter[i];
    }
    for (int i = 0; i < strlen(exit); i++) {
        borderMaze[height + 3][width - 3 + i] = exit[i];
    }

    return borderMaze;
}

// Function to print the maze
void printMaze(char** maze) {
    for (int i = 0; i < HEIGHT + 4; i++) {
        for (int j = 0; j < WIDTH + 4; j++) {
            printf("%c", maze[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int** maze = createMaze();
    char** borderedMaze = addBorderToMaze(maze);
    printMaze(borderedMaze);

    // Don't forget to free the memory!
    for (int i = 0; i < HEIGHT; i++) {
        free(maze[i]);
    }
    free(maze);
    for (int i = 0; i < HEIGHT + 4; i++) {
        free(borderedMaze[i]);
    }
    free(borderedMaze);

    return 0;
}
