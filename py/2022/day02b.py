total = 0

rps = ["A", "B", "C"]

for line in open(0):
    elf, me = line.split()

    if me == "X":
        total += (rps.index(elf) - 1) % 3 + 1
    elif me == "Y":
        total += rps.index(elf) + 1 + 3
    else:
        total += (rps.index(elf) + 1) % 3 + 1 + 6


print(total)
