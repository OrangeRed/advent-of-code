import re

lines = open(0).readlines()
copys = [1] * len(lines)

for card, line in enumerate(lines):
    _, winning_numbers, my_numbers = re.split(":|\|", line)
    winning_set = set(winning_numbers.split())
    my_set = set(my_numbers.split())

    matching = winning_set.intersection(my_set)
    if matching:
        for idx in range(len(matching)):
            copys[card + idx + 1] += 1 * copys[card]

print(sum(copys))
