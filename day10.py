with open("day10-input.txt") as f:
    values = f.read().splitlines()

# part 1
matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
rev_matches = {v: k for k, v in matches.items()}

inv_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points = 0
incomplete_lines = []

for l in values:
    # looks like we need a stack
    stack = []
    incomplete = True

    for c in l:
        if c in matches.keys():
            stack.append(c)
            continue

        last = stack.pop()
        if last != rev_matches[c]:
            # print(f"invalid line: {l} needed {last}, found {c}")
            points += inv_points[c]
            incomplete = False

            break

    if incomplete:
        incomplete_lines.append((l, stack.copy()))

print(points)

# part 2
inc_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

total_points = []

for l, s in incomplete_lines:
    points = 0

    for c in [matches[c] for c in reversed(s)]:
        points *= 5
        points += inc_points[c]

    total_points.append(points)

middle = sorted(total_points)[int(len(total_points) / 2)]
print(middle)