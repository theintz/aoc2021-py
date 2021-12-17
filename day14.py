from typing import Dict

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
def set_update(d: Dict, k: str, v: int = 1) -> Dict:
    d[k] = v if k not in d else d[k] + v
    return d

iterations = 40
counter_pairs = {}
counter_chars = {}
tf = {pair: [pair[0] + insert, insert + pair[1]] for pair, insert in transformations.items()}

for c in values[0]:
    counter_chars = set_update(counter_chars, c, 1)

for p in [values[0][i:i+2] for i in range(len(values[0]) - 1)]:
    counter_pairs = set_update(counter_pairs, p, 1)

for i in range(iterations):
    # print(counter_chars, counter_pairs)
    counter_n = {}

    for key, vals in tf.items():
        if key not in counter_pairs:
            continue

        counter_n = set_update(counter_n, vals[0], counter_pairs[key])
        counter_n = set_update(counter_n, vals[1], counter_pairs[key])
        counter_chars = set_update(counter_chars, vals[1][0], counter_pairs[key])
    
    counter_pairs = counter_n

print(max(counter_chars.values()) - min(counter_chars.values()))
