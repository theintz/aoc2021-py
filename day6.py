with open("day6-input.txt") as f:
    values = f.read().split(",")
    values = [int(v) for v in values]

# part 1
num_iterations = 80
fish = values.copy()

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