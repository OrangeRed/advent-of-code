import re

boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]
for sequence in open(0).read().strip().split(","):
    label, focal_len = re.split("=|-", sequence)

    value = 0
    for char in label:
        value = ((value + ord(char)) * 17) % 256

    lens_idx = -1
    for idx, (lens, _) in enumerate(boxes[value]):
        if lens == label:
            lens_idx = idx

    if not focal_len:
        if lens_idx != -1:
            boxes[value] = boxes[value][:lens_idx] + boxes[value][lens_idx + 1 :]
    else:
        if lens_idx != -1:
            boxes[value][lens_idx] = (label, int(focal_len))
        else:
            boxes[value].append((label, int(focal_len)))


total = 0
for box_idx, box in enumerate(boxes):
    for lens_idx, (lens, focal_len) in enumerate(box):
        total += focal_len * (box_idx + 1) * (lens_idx + 1)


print(total)
