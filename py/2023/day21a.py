grid = [[char for char in line] for line in open(0).read().splitlines()]
grid_h, grid_w = len(grid), len(grid[0])
start = 0, 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "S":
            start = x, y
            grid[y][x] = "."


STEPS = 64
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
plots = set([start])

for _ in range(STEPS):
    new_plots: set[tuple[int, int]] = set()
    for x, y in plots:
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if not (0 <= next_x < grid_w and 0 <= next_y < grid_h):
                continue

            if grid[next_y][next_x] not in ".":
                continue

            new_plots.add((next_x, next_y))

    plots = new_plots


print(len(plots))
