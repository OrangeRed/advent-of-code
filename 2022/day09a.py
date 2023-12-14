from typing import Tuple

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
unique: set[Tuple[int, int]] = set([(0, 0)])


def increment(delta: float) -> int:
    if delta > 0:
        return 1
    elif delta < 0:
        return -1
    else:
        return 0


head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
for line in open(0):
    move_x, move_y = directions[line[0]]
    steps = line.split()[1]

    for _ in range(int(steps)):
        head_x, head_y = head_x + move_x, head_y + move_y
        delta_x, delta_y = head_x - tail_x, head_y - tail_y
        distance = pow(delta_x, 2) + pow(delta_y, 2)
        if distance > 2:
            tail_x, tail_y = tail_x + increment(delta_x), tail_y + increment(delta_y)
            unique.add((tail_x, tail_y))


print(len(unique))
