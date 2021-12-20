from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open("day15-input.txt") as f:
    values = f.read().splitlines()
    values = [[int(v) for v in line] for line in values]

print(values)

# part 1
grid = Grid(matrix=values)
start = grid.node(0, 0)
end = grid.node(99, 99)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))
# print(path)

total = sum([values[y][x] for x, y in path])
print(total - 1)