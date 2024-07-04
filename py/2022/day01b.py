elves: list[int] = []

calories = 0
for line in open(0).read().splitlines() + [""]:
    if line:
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0


total = 0
for _ in range(3):
    total += max(elves)
    elves.remove(max(elves))


print(total)
