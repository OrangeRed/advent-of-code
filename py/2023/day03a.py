import re

total = 0

with open(0) as f:
    txt = f.read()
    lines = txt.splitlines()
    symbols = set(re.findall("(?!\d+|\.|\n).", txt))

    for row, line in enumerate(lines):
        for match in re.finditer("\d+", line):
            top = max(0, row - 1)
            left = max(0, match.start() - 1)
            bottom = min(len(lines), row + 1) + 1  # +1 because range() is exclusive
            right = min(len(line), match.end()) + 1  # +1 because range() is exclusive

            for schematic in lines[top:bottom]:
                if any(substr in schematic[left:right] for substr in symbols):
                    total += int(match.group())
                    break


print(total)
