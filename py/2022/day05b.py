import re

f = open(0).read().splitlines()

crates = f[: f.index("") - 1]
tower_bases = list(re.finditer("\d+", f[f.index("") - 1]))
towers: list[list[str]] = [[] for _ in tower_bases]
for line in reversed(crates):
    for idx, base in enumerate(tower_bases):
        crate = line[base.start()]
        if crate != " ":
            towers[idx].append(crate)


instructions = f[f.index("") + 1 :]
for line in instructions:
    amt, mvFrom, mvTo = [int(x) for x in re.findall("\d+", line)]

    mvCrates = towers[mvFrom - 1][-amt:]
    towers[mvFrom - 1] = towers[mvFrom - 1][:-amt]
    towers[mvTo - 1].extend(mvCrates)


print("".join(tower[-1] for tower in towers))
