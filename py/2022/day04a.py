import re

total = 0

for line in open(0):
    left_min, left_max, right_min, right_max = [int(x) for x in re.split("-|,", line)]

    left_set = set(range(left_min, left_max + 1))
    right_set = set(range(right_min, right_max + 1))

    if left_set.issubset(right_set) or right_set.issubset(left_set):
        total += 1


print(total)
