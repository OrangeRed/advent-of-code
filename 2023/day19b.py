from copy import deepcopy
from math import prod
import re

f = open(0).read().split("\n\n")

workflows = {
    k: v[:-1] for k, v in [workflow.split("{") for workflow in f[0].strip().split()]
}


def parseWorkflow(workflow: str, combinations: dict[str, set[int]]) -> int:
    *conditionals, last = workflow.split(",")

    accepted = 0
    for conditional in conditionals:
        key, value, out = re.split(">|<|:", conditional)
        target = deepcopy(combinations)
        target_range = (
            range(int(value)) if "<" in conditional else range(int(value) + 1, 4001)
        )

        target[key].intersection_update(target_range)
        combinations[key].difference_update(target_range)
        if out == "R":
            continue
        elif out == "A":
            accepted += prod(len(s) for s in target.values())
        else:
            accepted += parseWorkflow(workflows[out], target)

    if last == "R":
        return accepted
    elif last == "A":
        return accepted + prod(len(s) for s in combinations.values())
    else:
        return accepted + parseWorkflow(workflows[last], combinations)


print(parseWorkflow(workflows["in"], {k: set(range(1, 4001)) for k in "xmas"}))
