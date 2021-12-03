from typing import List

with open("day3-input.txt") as f:
    values = f.read().splitlines()
    values = [int(v, 2) for v in values]

def num_bits(values: List, index: int) -> int:
    return sum([1 if v & 1 << index else 0 for v in values])

def most_common_bit(values: List, index: int) -> int:
    return int(num_bits(values, index) >= len(values) / 2)

# part 1
gamma_list = reversed([most_common_bit(values, b) for b in range(12)])
gamma = int("".join(str(x) for x in gamma_list), 2)
epsilon = (gamma ^ 0xffff) & 0x0fff

print(gamma, epsilon, gamma * epsilon)

# part 2
oxy_values = values.copy()
co2_values = values.copy()

for i in range(11, -1, -1):
    if len(oxy_values) > 1:
        # figure out most and least common bit per digit
        mcb = most_common_bit(oxy_values, i)
        # filter out non-matching values
        oxy_values = [v for v in oxy_values if not bool((v & 1 << i) ^ (mcb << i))]
    
    if len(co2_values) > 1:
        # figure out most and least common bit per digit
        lcb = ~most_common_bit(co2_values, i) & 0x01
        # filter out non-matching values
        co2_values = [v for v in co2_values if not bool((v & 1 << i) ^ (lcb << i))]

print(oxy_values[0], co2_values[0], oxy_values[0] * co2_values[0])