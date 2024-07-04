from queue import Queue
import math


class Broadcaster:
    def __init__(self, outputs: list[str]):
        self.outputs = outputs

    def receive(self, src: str, pulse: int) -> list[tuple[str, int, str]]:
        return [(src, pulse, out) for out in self.outputs]


class FlipFlop:
    def __init__(self, outputs: list[str]):
        self.state = 0
        self.outputs = outputs

    def receive(self, src: str, pulse: int) -> list[tuple[str, int, str]]:
        if pulse:
            return []

        self.state = (self.state + 1) % 2
        return [(src, self.state, out) for out in self.outputs]


class Conjunction:
    def __init__(self, inputs: list[str], outputs: list[str]):
        self.inputs = {k: 0 for k in inputs}
        self.outputs = outputs

    def join(self, src: str, target: str, pulse: int) -> list[tuple[str, int, str]]:
        self.inputs[src] = pulse
        if all(self.inputs.values()):
            return [(target, 0, out) for out in self.outputs]
        else:
            return [(target, 1, out) for out in self.outputs]


f = [line.split(" -> ") for line in open(0).read().splitlines()]
Modules: dict[str, Broadcaster | Conjunction | FlipFlop] = {}

for module, _outputs in f:
    outputs = [out.strip() for out in _outputs.split(",")]
    if module == "broadcaster":
        Modules[module] = Broadcaster(outputs)
    elif "%" in module:
        Modules[module[1:]] = FlipFlop(outputs)
    else:
        inputs = [src[1:] for src, outputs in f if module[1:] in outputs]
        Modules[module[1:]] = Conjunction(inputs, outputs)


q: Queue[tuple[str, int, str]] = Queue()
presses = 0
# The machine turns on when a single low pulse is sent to rx.
# &cl, &rp, &lb, &nj -1-> &lx -0-> rx (Find when all inputs to &lx are 1)
lx_inputs: dict[str, int] = {}

while len(lx_inputs) != 4:
    presses += 1
    q.put(("button", 0, "broadcaster"))
    while not q.empty():
        src, pulse, target = q.get()
        if target == "lx" and pulse and src not in lx_inputs:
            lx_inputs[src] = presses

        mod = None if target not in Modules else Modules[target]
        if isinstance(mod, FlipFlop) or isinstance(mod, Broadcaster):
            for result in mod.receive(target, pulse):
                q.put(result)

        elif isinstance(mod, Conjunction):
            for result in mod.join(src, target, pulse):
                q.put(result)


print(math.lcm(*lx_inputs.values()))
