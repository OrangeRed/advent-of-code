from itertools import pairwise
import re

grid = [["."] * 1000 for _ in range(0, 1000)]
for rocks in [re.findall("\d+,\d+", line) for line in open(0).read().splitlines()]:
    for start, end in pairwise([coord.split(",") for coord in rocks]):
        (x1, y1), (x2, y2) = [int(i) for i in start], [int(i) for i in end]
        if (y1 - y2) == 0:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = "#"
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = "#"

total = 0
sand_x, sand_y = 500, 0
while sand_y + 1 < len(grid):
    if grid[sand_y + 1][sand_x] == ".":
        sand_y += 1
    elif grid[sand_y + 1][sand_x - 1] == ".":
        sand_y += 1
        sand_x -= 1
    elif grid[sand_y + 1][sand_x + 1] == ".":
        sand_y += 1
        sand_x += 1
    else:
        grid[sand_y][sand_x] = "O"
        sand_x, sand_y = 500, 0
        total += 1


print(total)
