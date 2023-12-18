# {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
# "0 means R, 1 means D, 2 means L, and 3 means U."
compass = [(1, 0), (0, 1), (-1, 0), (0, -1)]

vertices = [(0, 0)]
for line in open(0):
    _, hex_val = line.strip().split("#")
    distance, direction = int(hex_val[:-2], 16), int(hex_val[-2:-1])

    (x, y), (dx, dy) = vertices[-1], compass[direction]
    vertices.append((x + dx * distance, y + dy * distance))


# [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula)
area, perimeter = 0, 0
for (x1, y1), (x2, y2) in zip(vertices, vertices[1:]):
    area += (x1 * y2) - (x2 * y1)
    perimeter += abs(x1 - x2) + abs(y1 - y2)

# [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)
interior = area // 2 - perimeter // 2 + 1
print(perimeter + interior)
