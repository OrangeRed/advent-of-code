import re

f = open(0).read().split("\n\n")

seeds = []
for formula in re.findall("\d+\s\d+", f[0]):
    start, amt = [int(x) for x in formula.split()]
    seeds.append([start, start + amt - 1])


for line in f[1:]:
    for idx, [seed_start, seed_end] in enumerate(seeds):
        for mapping in re.findall("\d+\s\d+\s\d+", line):
            dest, src, r = [int(x) for x in mapping.split()]

            if seed_start >= src and seed_start < src + r:
                mapped_start = dest + (seed_start - src)
                if seed_end < src + r:
                    mapped_end = dest + (seed_end - src)
                    seeds[idx] = [mapped_start, mapped_end]
                else:
                    mapped_end = dest + r - 1
                    seeds[idx] = [mapped_start, mapped_end]
                    seeds.append([src + r, seed_end])
                break

            elif seed_start < src and seed_end > src:
                mapped_start = dest
                if seed_end < src + r:
                    mapped_end = dest + (seed_end - src)
                    seeds[idx] = [mapped_start, mapped_end]
                else:
                    mapped_end = dest + r - 1
                    seeds[idx] = [mapped_start, mapped_end]
                    seeds.append([src + r, seed_end])
                seeds.append([seed_start, src - 1])
                break


print(min(min(location) for location in seeds))
