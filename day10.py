with open("day10-input.txt") as f:
    values = f.read().splitlines()

# part 1
rev_matches = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}

inv_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# looks like we need a stack
stack = []
points = 0

for l in values:
    for c in l:
        if c in rev_matches.values():
            stack.append(c)
            continue

        if c not in rev_matches:
            print(f"char not recognized:{c} ")
            break
        
        last = stack.pop()
        if last != rev_matches[c]:
            print(f"invalid line: {l} needed {last}, found {c}")
            points += inv_points[c]

            break

print(points)