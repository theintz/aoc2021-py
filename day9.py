from math import prod

with open("day9-input.txt") as f:
    values = f.read().splitlines()
    values = [[int(v) for v in line] for line in values]

# part 1
dim_x = len(values[0])
dim_y = len(values)
lowpoints = []

total = 0
for y in range(dim_y):
    for x in range(dim_x):
        if x > 0 and values[y][x] >= values[y][x - 1]:
            continue
        
        if x < dim_x - 1 and values[y][x] >= values[y][x + 1]:
            continue
    
        if y > 0 and values[y][x] >= values[y - 1][x]:
            continue
        
        if y < dim_y - 1 and values[y][x] >= values[y + 1][x]:
            continue

        #print(f"lowpoint: x={x} y={y} value={values[y][x]}")
        lowpoints.append((x, y))
        total += 1 + values[y][x]

print(total)

# part 2
adjacencies = [(0, 1), (0, -1), (-1, 0), (1, 0)]
basin_sizes = []

for lp in lowpoints:
    basin_size = 0
    candidates = [lp]
    visited = []

    while len(candidates) > 0:
        basin_size += 1
        x, y = candidates.pop()
        visited.append((x, y))
        adj_coords = [(x + adj_x, y + adj_y) for adj_x, adj_y in adjacencies \
            if x + adj_x >= 0 and x + adj_x < dim_x and y + adj_y >= 0 and y + adj_y < dim_y]

        adj_valid = [(adj_x, adj_y) for adj_x, adj_y in adj_coords \
            if (adj_x, adj_y) not in visited and (adj_x, adj_y) not in candidates and values[adj_y][adj_x] != 9]
        candidates.extend(adj_valid)

        #print(x, y, adj_coords, adj_valid)

    # print(lp, basin_size)
    basin_sizes.append(basin_size)

print(prod(sorted(basin_sizes, reverse=True)[0:3]))
