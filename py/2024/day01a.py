def parseInput() -> tuple[list[int], list[int]]:
    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in open(0):
        left, right, *rest = line.split()
        left_numbers.append(int(left))
        right_numbers.append(int(right))

    return sorted(left_numbers), sorted(right_numbers)


if __name__ == "__main__":
    total: int = 0

    for left, right in zip(*parseInput()):
        total += abs(left - right)

    print(total)
