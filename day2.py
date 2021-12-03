with open("day2-input.txt") as f:
    values = f.read().splitlines()
    values = [v.split(" ") for v in values]

# part 1
hpos = 0
depth = 0

for (dir, amount) in values:
    hpos += int(amount) if dir == "forward" else 0
    depth += int(amount) if dir == "down" else 0
    depth -= int(amount) if dir == "up" else 0

print(hpos, depth, hpos * depth)

# part 2
hpos = 0
depth = 0
aim = 0

for (dir, amount) in values:
    if dir == "forward":
        hpos += int(amount)
        depth += aim * int(amount)
    elif dir == "down":
        aim += int(amount)
    elif dir == "up":
        aim -= int(amount)

print(hpos, depth, aim, hpos * depth)