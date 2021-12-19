from typing import Tuple

with open("day17-input.txt") as f:
    value = f.read()
    x_str = value.split(" ")[2]
    y_str = value.split(" ")[3]
    x_t = tuple([int(v) for v in x_str[2:-1].split("..")])
    y_t = tuple([int(v) for v in y_str[2:].split("..")])

# part 1
def in_bound(p: Tuple) -> bool:
    return p[0] in range(x_t[0], x_t[1] + 1) and p[1] in range(y_t[0], y_t[1] + 1)

max_overall_y = 0
iterations = 300

for traj_x, traj_y in [(a, b) for a in range(0, 200) for b in range(0, 200)]:
    x = 0
    y = 0
    max_y = 0
    
    for i in range(iterations):
        x += traj_x
        y += traj_y
        traj_x = 0 if traj_x == 0 else traj_x + 1 if traj_x < 0 else traj_x - 1
        traj_y = traj_y - 1
        max_y = y if y > max_y else max_y

        if in_bound((x, y)):
            max_overall_y = max_y if max_y > max_overall_y else max_overall_y
            break
    
print(max_overall_y)