def rotate(platform: list[list[str]], clockwise=True) -> list[list[str]]:
    rotated_platform: list[list[str]] = [[] for _ in platform[0]]

    if clockwise:
        for line in platform[::-1]:
            for idx, char in enumerate(line):
                rotated_platform[idx].append(char)
    else:
        for line in platform:
            for idx, char in enumerate(line[::-1]):
                rotated_platform[idx].append(char)

    return rotated_platform


def tilt_left(platform: list[list[str]]) -> list[list[str]]:
    for line in platform:
        empty_pos = 0
        for idx, char in enumerate(line):
            if char == "O":
                line[idx] = "."
                line[empty_pos] = "O"
                empty_pos += 1
            elif char == "#":
                empty_pos = idx + 1

    return platform


platform = [list(line) for line in open(0).read().splitlines()]
platform = rotate(platform, clockwise=False)  # Rotate once to make North face left
platform = tilt_left(platform)

total = 0
for line in platform:
    for idx, char in enumerate(line):
        if char == "O":
            total += len(line) - idx

print(total)
