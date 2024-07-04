import re


def compare(left: int | list, right: int | list) -> bool | None:
    if type(left) == int and type(right) == int:
        return None if left == right else left < right
    elif type(left) == list and type(right) == list:
        for x, y in zip(left, right):
            comparison = compare(x, y)
            if comparison != None:
                return comparison

        return None if len(left) == len(right) else len(left) < len(right)
    else:
        return compare(
            [left] if type(left) == int else left,
            [right] if type(right) == int else right,
        )


indices: list[int] = []
for idx, packets in enumerate(open(0).read().split("\n\n")):
    left, right = [eval(p) for p in packets.split()]

    if compare(left, right):
        indices.append(idx + 1)


print(sum(indices))
