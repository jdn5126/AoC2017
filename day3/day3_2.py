import sys


def update_grid(grid, x, y): 
    val = 0
    # Sum adjacent points
    for i in [-1, 0, 1]:
        try:
            grid[x + i]
        except KeyError:
            grid[x + i] = {}
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            else:
                try:
                    val += grid[x + i][y + j]
                except KeyError:
                    grid[x + i][y + j] = 0
    return val


def build_matrix(num):
    # Initialize grid
    grid = {}
    grid[0] = {}
    grid[0][0] = 1
    # Spiral
    x, y = 1, 0
    square = 1
    while True:
        # Up to square
        while y <= square:
            grid[x][y] = update_grid(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
            y += 1
        y -= 1
        # Left to -square
        while x >= (square * -1):
            grid[x][y] = update_grid(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
            x -= 1
        x += 1
        # Down to -square
        while y >= (square * -1):
            grid[x][y] = update_grid(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
            y -= 1
        y += 1
        # Right to square
        while x <= square:
            grid[x][y] = update_grid(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
            x += 1
        # Move to next square
        square += 1


if __name__ == "__main__":
    # Get input number
    num = int(sys.argv[1])
    # Build matrix
    print build_matrix(num)
