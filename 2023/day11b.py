from typing import Tuple

f = open(0).read().splitlines()
empty_cols: list[int] = []
for x, line in enumerate(reversed(f)):
    if "#" not in line:
        empty_cols.append(x)

rotated_f = ["".join(r) for r in list(zip(*f[::-1]))]
empty_rows: list[int] = []
for y, line in enumerate(rotated_f):
    if "#" not in line:
        empty_rows.append(y)


galaxies: list[Tuple[int, int]] = []
for y, row in enumerate(rotated_f):
    for x, char in enumerate(row):
        if char == "#":
            galaxies.append((int(x), int(y)))


total = 0
extra_dist = 1000000
for idx, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[idx + 1 :]:
        extra_x = sum(1 for x in empty_cols if max(x1, x2) > x and x > min(x1, x2))
        extra_y = sum(1 for y in empty_rows if max(y1, y2) > y and y > min(y1, y2))

        total += (
            abs(x2 - x1)
            + ((extra_dist - 1) * extra_x)
            + abs(y2 - y1)
            + ((extra_dist - 1) * extra_y)
        )


print(total)
