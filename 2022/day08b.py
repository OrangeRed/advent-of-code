f = open(0).read().splitlines()
grid = [[int(x) for x in row] for row in f]

total = 0


def getScore(trees: list[int]):
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            return score


for row_idx, row in enumerate(grid):
    for col_idx, height in enumerate(row):
        # Edge of grid
        if (
            row_idx == 0
            or col_idx == 0
            or row_idx == len(row) - 1
            or col_idx == len(grid) - 1
        ):
            continue

        left = row[:col_idx]
        right = row[col_idx + 1 :]
        # Create a list of values at col_idx
        col = [_row[col_idx] for _row in grid]
        top = col[:row_idx]
        bot = col[row_idx + 1 :]

        scenic_left = getScore(list(reversed(left)))
        scenic_right = getScore(right)
        scenic_top = getScore(list(reversed(top)))
        scenic_bot = getScore(bot)

        score = scenic_top * scenic_left * scenic_bot * scenic_right
        if score > total:
            total = score

print(total)
