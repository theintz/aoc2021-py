with open("day1-input.txt") as f:
    values = f.read().splitlines()
    values = [int(v) for v in values]

# part 1
prev = 0
count = 0
for i in values:
    if i > prev:
        count += 1
    prev = i

print(count - 1)

# part 2
prev = 0
count = 0
i = 2
while i < len(values):
    window = values[i - 2] + values[i - 1] + values[i]

    if window > prev:
        count += 1

    prev = window
    i += 1

print(count - 1)