with open("day9-input.txt") as f:
    values = f.read().splitlines()
    values = [[int(v) for v in line] for line in values]

# part 1
dim_x = len(values[0])
dim_y = len(values)

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

        print(f"lowpoint: x={x} y={y} value={values[y][x]}")
        total += 1 + values[y][x]

print(total)
