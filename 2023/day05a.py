import re

f = open(0).read().split("\n\n")
Map = {int(k): int(k) for k in re.findall("\d+", f[0])}

for line in f[1:]:
    for mapping in re.findall("\d+\s\d+\s\d+", line):
        dest, src, r = [int(x) for x in mapping.split()]
        for seed in Map:
            if seed >= src and seed <= src + r:
                Map[seed] = dest + (seed - src)

    Map = {v: v for v in Map.values()}


print(min(Map.values()))