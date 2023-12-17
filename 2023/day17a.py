import math
from heapq import heappush, heappop

Coords = tuple[int, int]
State = tuple[Coords, str, int]

grid = [[int(char) for char in line] for line in open(0).read().splitlines()]
grid_h, grid_w = len(grid), len(grid[0])

dirs = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}
turns = {
    "": ("R", "D"),
    "R": ("U", "D"),
    "L": ("D", "U"),
    "U": ("L", "R"),
    "D": ("R", "L"),
}


def getDirections(pos: Coords, direction: str, count: int) -> list[tuple[int, State]]:
    visited: list[tuple[int, State]] = []

    if direction:
        (x, y), (dx, dy) = pos, dirs[direction]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and count < 3:
            heat = grid[next_y][next_x]
            visited.append((heat, ((next_x, next_y), direction, count + 1)))

    for turn in turns[direction]:
        (x, y), (dx, dy) = pos, dirs[turn]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            heat = grid[next_y][next_x]
            visited.append((heat, ((next_x, next_y), turn, 1)))

    return visited


q: list[tuple[int, State]] = [(0, ((0, 0), "", 0))]
state: dict[State, int] = {((0, 0), "", 0): 0}
while q:
    heat, (pos, direction, count) = heappop(q)
    x, y = pos
    if x == grid_w - 1 and y == grid_h - 1:
        print(heat)
        break

    for extra_heat, visit in getDirections(pos, direction, count):
        if heat + extra_heat < state.get(visit, math.inf):
            state[visit] = heat + extra_heat
            heappush(q, (heat + extra_heat, visit))
