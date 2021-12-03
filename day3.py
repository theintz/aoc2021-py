with open("day3-input.txt") as f:
    values = f.read().splitlines()
    values = [int(v, 2) for v in values]

num_values = len(values)

# part 1
counters_bitset = {n: 0 for n in range(12)}

for v in values:
    for i in range(12):
        counters_bitset[i] += 1 if v & 1 << i else 0

gamma_list = [1 if c > num_values / 2 else 0 for c in counters_bitset.values()]
gamma = int("".join(str(x) for x in reversed(gamma_list)), 2)
epsilon = (gamma ^ 0xffff) & 0x0fff

print(gamma, epsilon, gamma * epsilon)

# part 2
