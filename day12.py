from typing import List

with open("day12-input.txt") as f:
    values = f.read().splitlines()
    values = [v.split("-") for v in values]

nodes = {}

for orig, dest in values:
    if orig in nodes:
        nodes[orig].append(dest)
    else:
        nodes[orig] = [dest]

    if dest in nodes:
        nodes[dest].append(orig)
    else:
        nodes[dest] = [orig]

print(nodes)

# part 1
paths = 0

# I am ashamed to admit that I don't understand entirely why this works, but it does.
# However, I could not figure out what needs to be returned, so I have to resort to
# a nasty global variable
def traverse(node: str, path: List, visited: List):
    global paths

    # print("ENTRY", node, path, visited)
    if node == "end":
        # print("DONE", path)
        paths += 1
        return

    if node.islower() and node in visited:
        return

    [traverse(cand, path + [cand], visited + [node]) for cand in nodes[node]]

traverse("start", ["start"], [])
print(paths)
