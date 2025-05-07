def parseInput() -> tuple[dict[int, int], list[int]]:
    similarity: dict[int, int] = {}
    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in open(0):
        left, right, *rest = line.split()

        if left not in similarity:
            similarity[int(left)] = 0

        left_numbers.append(int(left))
        right_numbers.append(int(right))

    for number in right_numbers:
        if number in left_numbers:
            similarity[number] += 1

    return similarity, left_numbers


if __name__ == "__main__":
    total: int = 0

    similarity, left_numbers = parseInput()
    for number in left_numbers:
        total += number * similarity[number]

    print(total)
