from typing import List

with open("day3-input.txt") as f:
    values = f.read().splitlines()
    values = [int(v, 2) for v in values]

def most_common_bit(values: List, index: int) -> int:
    return int(sum([1 if v & 1 << index else 0 for v in values]) > len(values) / 2)

# part 1
gamma_list = [most_common_bit(values, b) for b in range(12)]
gamma = int("".join(str(x) for x in reversed(gamma_list)), 2)
epsilon = (gamma ^ 0xffff) & 0x0fff

print(gamma, epsilon, gamma * epsilon)

# part 2
