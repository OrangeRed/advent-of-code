import re

f = open(0).read().split("\n\n")

workflows = {
    k: v[:-1] for k, v in [workflow.split("{") for workflow in f[0].strip().split()]
}


def parseWorkflow(workflow: str, part: dict[str, int]) -> str:
    *conditionals, last = workflow.split(",")
    for conditional in conditionals:
        key, value, out = re.split(">|<|:", conditional)
        if ">" in conditional and part[key] > int(value):
            return out
        elif "<" in conditional and part[key] < int(value):
            return out

    return last


total = 0
for ratings in [line[1:-1].split(",") for line in f[1].strip().split()]:
    part = {k: int(v) for k, v in [category.split("=") for category in ratings]}

    key = "in"
    while not (key == "A" or key == "R"):
        key = parseWorkflow(workflows[key], part)

    if key == "A":
        total += sum(part.values())


print(total)
