from typing import Tuple
import re

f = open(0).read().split("\n\n")

jump_map: dict[str, Tuple[str, str]] = {}
for line in f[1].strip().split("\n"):
    src, left, right = re.findall("[A-Z]{3}", line)
    jump_map[src] = (left, right)


src = "AAA"
jumps = 0
while src != "ZZZ":
    for instruction in f[0]:
        src = jump_map[src][0] if instruction == "L" else jump_map[src][1]
        jumps += 1


print(jumps)
