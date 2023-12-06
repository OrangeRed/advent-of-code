import re

total = 0

for card, line in enumerate(open(0)):
    _, winning_numbers, my_numbers = re.split(":|\|", line)
    winning_set = set(winning_numbers.split())
    my_set = set(my_numbers.split())

    matching = winning_set.intersection(my_set)
    if matching:
        total += pow(2, len(matching) - 1)

print(total)
