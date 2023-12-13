def validReflection(pattern: list[str], location: int) -> bool:
    dist_to_end = min(location + 1, len(pattern) - (location + 1))
    left = "".join(pattern[location - (dist_to_end - 1) : location + 1])
    right = "".join(pattern[location + 1 : location + dist_to_end + 1][::-1])

    return left == right


total = 0
for pattern in [p.split() for p in open(0).read().split("\n\n")]:
    rows, cols = 0, 0

    for idx, _ in enumerate(pattern[1:]):
        if pattern[idx] == pattern[idx + 1] and validReflection(pattern, idx):
            rows = idx + 1
            break

    if rows:
        total += 100 * rows
        continue

    pattern = ["".join(r) for r in zip(*pattern[::-1])]
    for idx, _ in enumerate(pattern[1:]):
        if pattern[idx] == pattern[idx + 1] and validReflection(pattern, idx):
            cols = idx + 1
            break

    total += cols


print(total)
