from typing import Tuple
from functools import reduce
import math
import re

f = open(0).read().split("\n\n")

jump_map: dict[str, Tuple[str, str]] = {}
sources: list[str] = []
for line in f[1].strip().split("\n"):
    src, left, right = re.findall("[0-9A-Z]{3}", line)
    jump_map[src] = (left, right)
    if src[-1] == "A":
        sources.append(src)


jumps = [0 for _ in sources]
for idx, src in enumerate(sources):
    while src[-1] != "Z":
        for instruction in f[0]:
            src = jump_map[src][0] if instruction == "L" else jump_map[src][1]
            jumps[idx] += 1

            if src[-1] == "Z":
                break


print(reduce(lambda x, y: math.lcm(x, y), jumps))
