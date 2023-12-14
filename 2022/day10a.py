lines = open(0).read().splitlines()
total_cycles = lines.count("noop") + (len(lines) - lines.count("noop")) * 2

upcoming: dict[int, int] = {}
xregister, cycle = 1, 0

total = 0

for i in range(0, total_cycles):
    if i % 40 == 20:
        total += i * xregister

    if i in upcoming:
        xregister += upcoming[i]

    cmd = lines[i] if i < len(lines) else "noop"
    if cmd != "noop":
        increment = cmd.split()[1]
        upcoming[cycle + 2] = int(increment)
        cycle += 2
    else:
        cycle += 1


print(total)
