import re
import math

f = open(0).read().splitlines()
time = int("".join(re.findall("\d+", f[0])))
distance = int("".join(re.findall("\d+", f[1])))


def findRoots(b: int, c: int) -> int:
    discriminant = pow(b, 2) - 4 * c
    if discriminant < 0:
        return 0
    else:
        leftRoot = (-b - math.sqrt(discriminant)) / 2
        rightRoot = (-b + math.sqrt(discriminant)) / 2
        return math.ceil(rightRoot) - math.floor(leftRoot) - 1


total = findRoots(-time, distance)
print(total)
