from math import floor
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


packets = ["[[2]]", "[[6]]"]
for new_packet in open(0).read().replace("\n\n", "\n").splitlines():
    # # This linear search is slow but answers the question
    # idx = 0
    # for packet in packets:
    #     if compare(eval(new_packet), eval(packet)):
    #         break
    #     idx += 1
    #
    # packets.insert(idx, new_packet)

    # Faster binary search implementaion
    left, right = 0, len(packets)
    while left != right:
        middle = floor((left + right) / 2)
        if compare(eval(new_packet), eval(packets[middle])):
            right = middle
        else:
            left = middle + 1

    packets.insert(left, new_packet)

print((packets.index("[[2]]") + 1) * (packets.index("[[6]]") + 1))
