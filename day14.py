from typing import List

with open("day14-input.txt") as f:
    values = f.read().splitlines()
    polymer = values[0]
    transformations = dict([tuple(v.split(" -> ")) for v in values[2:]])

# part 1
iterations = 10

for i in range(iterations):
    pairs = [polymer[i:i+2] for i in range(len(polymer) - 1)]    
    polymer = "".join([p[0] + transformations[p] if p in transformations else "" for p in pairs]) + polymer[-1]

counts = [polymer.count(c) for c in set(polymer)]
print(len(polymer), max(counts) - min(counts))

# part 2