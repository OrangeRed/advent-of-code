from itertools import combinations


def compareStrings(spring: str, opt: str) -> bool:
    for spring_char, opt_char in zip(spring, opt):
        if spring_char == "#" and opt_char != "#":
            return False
        elif spring_char == "." and opt_char != ".":
            return False

    return True


total = 0
for springs, _records in [line.split() for line in open(0).read().splitlines()]:
    records = eval(_records)
    no_empty = len(springs) - sum(records) - (len(records) - 1)

    for c in combinations(range(len(records) + no_empty), len(records)):
        selected = [-1] * (len(records) + no_empty)
        pos_idx = 0
        for pos in c:
            selected[pos] = pos_idx
            pos_idx += 1

        opt = ""
        for pos in selected:
            opt += "#" * records[pos] if pos > -1 else ""
            opt += "."

        if compareStrings(springs, opt[:-1]):
            total += 1


print(total)
