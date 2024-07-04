total = 0
for sequence in open(0).read().strip().split(","):
    value = 0
    for char in sequence:
        value = ((value + ord(char)) * 17) % 256

    total += value


print(total)
