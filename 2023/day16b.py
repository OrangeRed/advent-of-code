Coord = tuple[int, int]
Move = tuple[Coord, Coord]

grid = [[char for char in line] for line in open(0).read().splitlines()]
grid_h, grid_w = len(grid), len(grid[0])

back_slash = lambda x, y: (y, x)
forward_slash = lambda x, y: (-y, -x)


def energize(start: Coord, direction: Coord) -> int:
    visited: set[Move] = set()
    moves: list[Move] = [(start, direction)]

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
    return len(energized)


energized: list[int] = []
for i in range(grid_h):
    energized.append(energize((-1, i), (1, 0)))
    energized.append(energize((grid_w, i), (-1, 0)))

for i in range(grid_w):
    energized.append(energize((i, -1), (0, 1)))
    energized.append(energize((i, grid_h), (0, -1)))

print(max(energized))
