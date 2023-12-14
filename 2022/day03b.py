alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper()

total = 0

rugsacks = open(0).read().splitlines()
for idx in range(0, len(rugsacks), 3):
    for char in set(rugsacks[idx]) & set(rugsacks[idx + 1]) & set(rugsacks[idx + 2]):
        total += alpha.index(char) + 1


print(total)
