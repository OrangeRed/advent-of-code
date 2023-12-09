total = 0

for line in open(0):
    numbers = [int(x) for x in line.split()]
    firsts = [numbers[0]]
    while not all([n == 0 for n in numbers]):
        numbers = [numbers[i + 1] - numbers[i] for i, _ in enumerate(numbers[:-1])]
        firsts.append(numbers[0])

    for idx, first in enumerate(firsts):
        total += first * (1 if idx % 2 == 0 else -1)


print(total)
