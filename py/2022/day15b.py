from typing import Tuple
import re

Coords = Tuple[int, int]

search_start, search_end = 0, 4000000
f = [re.findall("-?[0-9]\d*", line) for line in open(0).read().splitlines()]

positive_lines: set[int] = set()
negative_lines: set[int] = set()
for sx, sy, bx, by in [map(int, coords) for coords in f]:
    dist_to_beacon = abs(sx - bx) + abs(sy - by)
    left, right = sx - dist_to_beacon - 1, sx + dist_to_beacon + 1
    # top, bottom = sy - dist_to_beacon - 1, sy + dist_to_beacon + 1

    # y = x + b -> b = y - x
    positive_lines.update([sy - left, sy - right])
    # y = -x + c -> c = y + x
    negative_lines.update([sy + left, sy + right])


points: set[Coords] = set()
for b in positive_lines:
    for c in negative_lines:
        y = (b + c) // 2
        x = y - b
        if search_start < x < search_end and search_start < y < search_end:
            points.add((x, y))


points_to_remove: set[Coords] = set()
for sx, sy, bx, by in [map(int, coords) for coords in f]:
    dist_to_beacon = abs(sx - bx) + abs(sy - by)
    for x, y in points:
        dist_to_point = abs(sx - x) + abs(sy - y)
        if dist_to_point <= dist_to_beacon:
            points_to_remove.add((x, y))

    points = points.difference(points_to_remove)
    points_to_remove.clear()


print(*(x * 4000000 + y for x, y in points))
