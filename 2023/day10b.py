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
vertices = [(start_x, start_y)]
stack = [(start_x, start_y)]
while stack:
    x, y = stack.pop()
    visited.add((x, y))
    pipe = grid[y][x]
    if pipe in "LJ7F":
        vertices.append((x, y))

    for dx, dy in directions[pipe]:
        if (x + dx, y + dy) in visited:
            continue

        next_pipe = grid[y + dy][x + dx]
        if next_pipe != "." and (-dx, -dy) in directions[next_pipe]:
            stack.append((x + dx, y + dy))


# [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula)
area = 0
for i in range(0, len(vertices)):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % len(vertices)]
    area += (x2 * y1) - (x1 * y2)

# [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)
print(int(area / 2 - len(visited) / 2 + 1))
