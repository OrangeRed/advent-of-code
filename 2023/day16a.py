Coord = tuple[int, int]
Move = tuple[Coord, Coord]

grid = [[char for char in line] for line in open(0).read().splitlines()]
grid_h, grid_w = len(grid), len(grid[0])

back_slash = lambda x, y: (y, x)
forward_slash = lambda x, y: (-y, -x)

visited: set[Move] = set()
moves: list[Move] = [((-1, 0), (1, 0))]

while moves:
    (x, y), (dx, dy) = moves.pop()

    next_x, next_y = x + dx, y + dy
    if not (0 <= next_x < grid_w and 0 <= next_y < grid_h):
        continue

    if ((next_x, next_y), (dx, dy)) in visited:
        continue

    visited.add(((next_x, next_y), (dx, dy)))

    splitter = "|" if dx else "-"
    char = grid[next_y][next_x]

    if char == "/":
        moves.append(((next_x, next_y), forward_slash(dx, dy)))
    elif char == "\\":
        moves.append(((next_x, next_y), back_slash(dx, dy)))
    elif char == splitter:
        moves.append(((next_x, next_y), forward_slash(dx, dy)))
        moves.append(((next_x, next_y), back_slash(dx, dy)))
    else:
        moves.append(((next_x, next_y), (dx, dy)))


# Dedupe points
energized = set(point for (point, _) in visited)
print(len(energized))
