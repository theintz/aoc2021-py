from statistics import median

with open("day7-input.txt") as f:
    values = f.read().split(",")
    values = [int(v) for v in values]

# part 1
med = int(median(values))
diff = sum([abs(v - med) for v in values])
print(diff)
