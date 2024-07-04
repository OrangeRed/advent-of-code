f = open(0).read().splitlines()
grid = [[int(x) for x in row] for row in f]

total = 0
for row_idx, row in enumerate(grid):
    for col_idx, height in enumerate(row):
        # Edge of grid
        if (
            row_idx == 0
            or col_idx == 0
            or row_idx == len(row) - 1
            or col_idx == len(grid) - 1
        ):
            total += 1
            continue

        left = row[:col_idx]
        right = row[col_idx + 1 :]
        # Create a list of values at col_idx
        col = [_row[col_idx] for _row in grid]
        top = col[:row_idx]
        bot = col[row_idx + 1 :]

        # Left
        if height > max(left):
            total += 1
        # Right
        elif height > max(right):
            total += 1
        # Top
        elif height > max(top):
            total += 1
        # Bottom
        elif height > max(bot):
            total += 1


print(total)
