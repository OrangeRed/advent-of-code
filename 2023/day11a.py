from typing import Tuple


grid: list[str] = []
for line in open(0).read().splitlines():
    grid.append(line)
    if "#" not in line:
        grid.append(line)

rotated_grid = ["".join(r) for r in list(zip(*grid[::-1]))]
expanded_grid: list[str] = []
for line in rotated_grid:
    expanded_grid.append(line)
    if "#" not in line:
        expanded_grid.append(line)


galaxies: list[Tuple[int, int]] = []
for y, row in enumerate(expanded_grid):
    for x, char in enumerate(row):
        if char == "#":
            galaxies.append((int(x), int(y)))


total = 0
for idx, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[idx + 1 :]:
        total += abs(x2 - x1) + abs(y2 - y1)


print(total)
