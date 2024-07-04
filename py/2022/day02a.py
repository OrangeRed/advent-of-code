total = 0

rps = ["A", "B", "C"]

for line in open(0):
    elf, me = line.replace("X", "A").replace("Y", "B").replace("Z", "C").split()

    if (rps.index(me) - rps.index(elf)) % 3 == 1:
        total += rps.index(me) + 1 + 6
    elif rps.index(me) == rps.index(elf):
        total += rps.index(me) + 1 + 3
    else:
        total += rps.index(me) + 1


print(total)
