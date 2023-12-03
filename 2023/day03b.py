import re

total = 0

with open(0) as f:
    txt = f.read()
    lines = txt.splitlines()

    gears: list[dict[str, int]] = []
    for row, line in enumerate(lines):
        for found_gear in re.finditer("\*", line):
            gears.append({"x": found_gear.start(), "y": row, "number": 0})

    for row, line in enumerate(lines):
        for match in re.finditer("\d+", line):
            top = max(0, row - 1)
            left = max(0, match.start() - 1)
            bottom = min(len(lines), row + 1) + 1  # +1 because range() is exclusive
            right = min(len(line), match.end()) + 1  # +1 because range() is exclusive

            for gear in gears:
                if gear["x"] in range(left, right) and gear["y"] in range(top, bottom):
                    if gear["number"] == 0:
                        gear["number"] = int(match.group())
                    else:
                        total += gear["number"] * int(match.group())
                    break


print(total)
