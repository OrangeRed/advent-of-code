alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper()

total = 0

for line in open(0).read().splitlines():
    for char in set(line[: len(line) // 2]) & set(line[len(line) // 2 :]):
        total += alpha.index(char) + 1


print(total)
