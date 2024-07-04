lines = open(0).read().splitlines()
total_cycles = 2 * len(lines) - lines.count("noop")

upcoming: dict[int, int] = {}
xregister, cycle = 1, 0

total = 0

strings: list[str] = []
current_string = ""

for i in range(0, 241):
    if i > 0 and i % 40 == 0:
        strings.append(current_string)
        current_string = ""

    if i in upcoming:
        xregister += upcoming[i]

    cmd = lines[i] if i < len(lines) else "noop"
    if cmd != "noop":
        increment = cmd.split()[1]
        upcoming[cycle + 2] = int(increment)
        cycle += 2
    else:
        cycle += 1

    pixel = len(current_string)
    if pixel in range(xregister - 1, xregister + 2):
        current_string += "#"
    else:
        current_string += "."


print("\n".join(strings))
