import re

total = 0

words = "one two three four five six seven eight nine".split()


def convert_to_int(x: str) -> int:
    if x in words:
        return words.index(x) + 1
    else:
        return int(x)


for line in open(0):
    digits = re.findall(f"(?=({ '|'.join(words) }|\\d))", line)

    tens_place = convert_to_int(digits[0]) * 10
    ones_place = convert_to_int(digits[-1])

    total += tens_place + ones_place

print(total)
