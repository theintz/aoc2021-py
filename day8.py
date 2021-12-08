with open("day8-input.txt") as f:
    values = f.read().splitlines()
    values = [v.split(" | ") for v in values]
    values = [(v[0].split(" "), v[1].split(" ")) for v in values]

# part 1
count = sum([len([r for r in result if len(r) in (2, 3, 4, 7)]) for _, result in values])
print(count)