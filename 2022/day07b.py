# Create Tree
root: dict = {}
tree = root
path: list[str] = []
dirs: dict[str, int] = {}

for line in open(0).read().splitlines()[1:]:
    cmd, dest = line.strip().split()[-2:]

    if cmd.isdigit():
        tree[dest] = int(cmd)
    elif cmd == "dir":
        tree[dest] = {}
    elif cmd == "cd" and dest != "..":
        path.append(dest)
        tree = tree[dest]
    elif cmd == "cd" and dest == "..":
        path.pop()
        tree = root
        for step in path:
            tree = tree[step]


def sumTree(subtree: dict) -> int:
    total = 0
    for v in subtree.values():
        if type(v) == dict:
            total += sumTree(v)
        else:
            total += v
    return total


def getDirSizes(name: str, subtree: dict):
    dirs[name] = sumTree(subtree)

    for key, leaf in subtree.items():
        if type(leaf) == dict:
            getDirSizes(name + key + "/", leaf)


getDirSizes("/", root)
root_disk = sumTree(root)
for disk_space in sorted(list(dirs.values())):
    if 40000000 >= root_disk - disk_space:
        print(disk_space)
        break
