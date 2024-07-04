start_x, start_y = 0, 0
grid: list[str] = []
for y, line in enumerate(open(0).read().splitlines()):
    grid.append(line)
    if line.find("S") != -1:
        start_x, start_y = line.find("S"), y

directions = {
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)],
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

visited = set([(start_x, start_y)])
stack = [(start_x, start_y)]
while stack:
    x, y = stack.pop()
    visited.add((x, y))
    pipe = grid[y][x]
    for dx, dy in directions[pipe]:
        if (x + dx, y + dy) in visited:
            continue

        next_pipe = grid[y + dy][x + dx]
        if next_pipe != "." and (-dx, -dy) in directions[next_pipe]:
            stack.append((x + dx, y + dy))


print(int(len(visited) / 2))
