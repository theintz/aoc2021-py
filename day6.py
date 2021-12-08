from collections import deque

with open("day6-input.txt") as f:
    values = f.read().split(",")
    values = [int(v) for v in values]

# part 1
num_iterations = 80
fish = values.copy()

# naive implementation
for _ in range(num_iterations):
    new_fish = 0

    for i in range(len(fish)):
        if fish[i] > 0:
            fish[i] -= 1
        else:
            fish[i] = 6
            new_fish += 1

    fish.extend([8] * new_fish)
    new_fish = 0

print(len(fish))

# part 2
num_iterations = 256
fish = deque([values.count(n) for n in range(9)])

# much better implementation
for _ in range(num_iterations):
    # num of fish who were change to 0 in last iteration
    new_fish = fish.popleft()

    fish[6] += new_fish
    fish.append(new_fish)

print(sum(fish))