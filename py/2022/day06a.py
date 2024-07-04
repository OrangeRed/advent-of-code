import re

buffer = open(0).read()

for idx, _ in enumerate(buffer):
    unique_chars = set(buffer[idx : min(len(buffer), idx + 4)])
    if len(unique_chars) == 4:
        print(idx + 4)
        break
