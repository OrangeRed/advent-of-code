import re

target_y = 2000000
ranges: set[int] = set()

for coords in [re.findall("-?[0-9]\d*", line) for line in open(0).read().splitlines()]:
    sx, sy, bx, by = map(int, coords)

    if sy == target_y:
        ranges.add(sy)
    elif by == target_y:
        ranges.add(by)

    dist_from_beacon = abs(sx - bx) + abs(sy - by)
    dist_from_target = abs(target_y - sy)
    if dist_from_target <= dist_from_beacon:
        ranges.update(
            range(
                sx - (dist_from_beacon - dist_from_target),
                sx + (dist_from_beacon - dist_from_target),
            )
        )

print(len(ranges))
