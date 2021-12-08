from statistics import median

with open("day7-input.txt") as f:
    values = f.read().split(",")
    values = [int(v) for v in values]

# part 1
med = int(median(values))
diff = sum([abs(v - med) for v in values])
print(diff)

# part 2
# there is probably a very clean math based solution for this, but I can't think
# of it, so I'll brute-force the solution

best_target = 0
best_target_sum = 999999999

for target in range(200, 1200):
    diff = sum([sum(range(1, abs(v - target) + 1)) for v in values])

    if diff < best_target_sum:
        best_target = target
        best_target_sum = diff

print(best_target, best_target_sum)