elves: list[int] = []

calories = 0
for line in open(0).read().splitlines() + [""]:
    if line:
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0


print(max(elves))
