import re

buffer = open(0).read()

for idx, _ in enumerate(buffer):
    unique_chars = set(buffer[idx : min(len(buffer), idx + 14)])
    if len(unique_chars) == 14:
        print(idx + 14)
        break
