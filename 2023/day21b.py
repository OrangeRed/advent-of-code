grid = [[char for char in line] for line in open(0).read().splitlines()]
grid_h, grid_w = len(grid), len(grid[0])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
plots = set([(grid_w // 2, grid_h // 2)])
# Since grid repeats itself you can create a polynomial to calculate plots
# Grid repeats itself every 131 (grid_w), position of S is 65 (grid_w // 2)
# So get values for three points f(65), f(65 + 131), f(65 + 131 * 2) for Lagrange's
points: list[int] = []

for i in range(grid_w * 2 + grid_w // 2):
    new_plots: set[tuple[int, int]] = set()
    for x, y in plots:
        for dx, dy in directions:
            next_x, next_y = (x + dx) % grid_w, (y + dy) % grid_h

            if grid[next_y][next_x] not in "SO.":
                continue

            grid[next_y][next_x] = "O"
            new_plots.add((x + dx, y + dy))

    plots = new_plots
    # +1 because range starts at 0
    if i % grid_w + 1 == (grid_w // 2):
        points.append(len(plots))


# https://old.reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/keb8ud3
# Lagrange's Interpolation formula for ax^2 + bx + c with x=[0,1,2] and y=[y0,y1,y2]
# f(x) = (x^2-3x+2) * y0 / 2 - (x^2-2x) * y1 + (x^2-x) * y2 / 2
# f(x) = (y0 / 2 - y1 + y2 / 2)x^2 + (-3/2 * y0 + 2 * y1 - y2 / 2)x + (y0)
#
# a = y0 / 2 - y1 + y2 / 2
# b = -3/2 * y0 + 2 * y1 - y2 / 2
# c = y0
a = points[0] / 2 - points[1] + points[2] / 2
b = -3 / 2 * points[0] + 2 * points[1] - points[2] / 2
c = points[0]


STEPS = 26501365 // grid_w
print(round(a * (STEPS**2) + b * STEPS + c))
