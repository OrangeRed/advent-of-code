from functools import cache


@cache
def getCombos(springs: str, records: tuple[int], done_springs=0) -> int:
    if not springs:
        # +1 if all records were consumed and there are no remaining springs
        if len(records) == 0 and done_springs == 0:
            return 1
        # +1 if the last record is the same size as the last spring
        elif len(records) == 1 and records[0] == done_springs:
            return 1
        else:
            return 0

    count = 0
    possible = [".", "#"] if springs[0] == "?" else springs[0]
    for char in possible:
        if char == "#":
            # Extend current spring
            count += getCombos(springs[1:], records, done_springs + 1)
        else:
            if done_springs > 0:
                # Complete current spring and move onto the next one
                if records and records[0] == done_springs:
                    count += getCombos(springs[1:], records[1:])
            else:
                # if not working on a spring move onto the next symbol
                count += getCombos(springs[1:], records)

    return count


total = 0
for springs, _records in [line.split() for line in open(0).read().splitlines()]:
    springs += ("?" + springs) * 4
    records = eval(_records) * 5

    c = getCombos(springs, records)
    # print(c)
    total += c

print(total)
