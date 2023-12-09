total = 0

for line in open(0):
    numbers = [int(x) for x in line.split()]
    lasts = [numbers[-1]]
    while not all([n == 0 for n in numbers]):
        numbers = [numbers[i + 1] - numbers[i] for i, _ in enumerate(numbers[:-1])]
        lasts.append(numbers[-1])

    total += sum(lasts)


print(total)
