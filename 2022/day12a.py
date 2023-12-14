from queue import Queue
from typing import Tuple

Coords = Tuple[int, int]

height = "SabcdefghijklmnopqrstuvwxyzE"

grid: list[list[str]] = []
path: Queue[Tuple[Coords, int]] = Queue()
seen: set[Coords] = set([])

for y, row in enumerate(open(0).read().splitlines()):
    grid.append([])
    for x, char in enumerate(row):
        grid[y].append(char)
        if char == "S":
            seen.add((x, y))
            path.put(((x, y), 0))


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while not path.empty():
    moves: list[Tuple[Coords, int]] = []
    (curr_x, curr_y), step = path.get()

    if grid[curr_y][curr_x] == "E":
        print(step)
        break

    for dx, dy in directions:
        next_x, next_y = curr_x + dx, curr_y + dy
        # Skip steps that are out of bounds
        if next_x < 0 or next_x >= len(grid[0]) or next_y < 0 or next_y >= len(grid):
            continue

        # Skip steps that have a height difference of more than 1
        if height.find(grid[curr_y][curr_x]) + 1 < height.find(grid[next_y][next_x]):
            continue

        moves.append(((next_x, next_y), step + 1))

    for move, step in moves:
        if move not in seen:
            seen.add(move)
            path.put((move, step))
