import operator
import math
import re


class Monkey:
    def __init__(self, monkey_stats: list[str]):
        self.items = [int(x) for x in re.findall("\d+", monkey_stats[1])]
        self.calc = monkey_stats[2]
        self.divisor = [int(x) for x in re.findall("\d+", monkey_stats[3])][0]
        self.trueTarget = int(monkey_stats[4].strip()[-1])
        self.falseTarget = int(monkey_stats[5].strip()[-1])
        self.inspects = 0

    def doCalc(self, item: int, prime: int) -> int:
        l, o, r = self.calc.split("=")[1].split()
        left = int(l) if l.isdigit() else item
        right = int(r) if r.isdigit() else item
        res = operators[o](left % prime, right % prime)
        return res % prime

    def testItem(self, item: int) -> int:
        return self.trueTarget if item % self.divisor == 0 else self.falseTarget


operators = {"+": operator.add, "*": operator.mul}
monkeys: list[Monkey] = [Monkey(m.splitlines()) for m in open(0).read().split("\n\n")]
prime = math.prod([m.divisor for m in monkeys])


for rounds in range(0, 10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspects += 1
            item = monkey.doCalc(item, prime)
            target = monkey.testItem(item)
            monkeys[target].items.append(item)
        monkey.items.clear()


inspects = sorted([monkey.inspects for monkey in monkeys])
print(inspects[-1] * inspects[-2])
