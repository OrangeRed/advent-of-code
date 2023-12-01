import re

total = 0

for line in open(0):
    digits = re.findall("\d", line)

    total += int(digits[0]) * 10 + int(digits[-1])

print(total)
