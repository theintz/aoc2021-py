from typing import List, Tuple

with open("day11-input.txt") as f:
    values = f.read().splitlines()
    values = [[int(v) for v in line] for line in values]

# part 1
dim_x = len(values[0])
dim_y = len(values)
iterations = 100
octopi = values.copy()
total_flashes = 0

adjacencies = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]

def get_adj_coords(x: int, y: int) -> List[Tuple]:
    return [(x + x_adj, y + y_adj) for x_adj, y_adj in adjacencies \
        if x + x_adj >= 0 and x + x_adj < dim_x and y + y_adj >= 0 and y + y_adj < dim_y]


for i in range(iterations):
    # increase all levels
    for y in range(dim_y):
        for x in range(dim_x):
            octopi[y][x] += 1

    flashes = 0
    flashed = True
    flashers = []

    # flash all octopi
    while flashed:
        flashed = False

        for y in range(dim_y):
            for x in range(dim_x):
                if octopi[y][x] > 9:
                    # print("flash ", x, y)
                    flashes += 1
                    flashed = True
                    flashers.append((x, y))

                    for nb_x, nb_y in get_adj_coords(x, y):
                        octopi[nb_y][nb_x] += 1
                    
                    octopi[y][x] = 0
    
    # reset those that have flashed, their levels may have been increased again
    for x_f, y_f in flashers:
        octopi[y_f][x_f] = 0

    total_flashes += flashes

print(total_flashes)
    
