from typing import List, Optional, Tuple

with open("day5-input.txt") as f:
    values = f.read().splitlines()
    values = [v.replace(" -> ", ",").split(",") for v in values]
    values = [[int(v) for v in l] for l in values]
    values = [((v[0], v[1]), (v[2], v[3])) for v in values]


def interpolate_points(orig: Tuple, dest: Tuple) -> Optional[List[Tuple]]:
    """ Returns a list of all the points in between orig and dest, or None
    if the points aren't horizontal or vertical. """
    x_orig, y_orig = orig
    x_dest, y_dest = dest

    if x_orig == x_dest:
        dir = 1 if y_orig < y_dest else -1
        return [(x_orig, y) for y in range(y_orig, y_dest + dir, dir)]
    elif y_orig == y_dest:
        dir = 1 if x_orig < x_dest else -1
        return [(x, y_orig) for x in range(x_orig, x_dest + dir, dir)]
    else:
        return None

def test_interpolate():
    horizontal = [(1, 1), (2, 1), (3, 1)]
    interpolate_horizontal = interpolate_points((1, 1), (3, 1))
    assert(interpolate_horizontal == horizontal)

    backwards = [(9, 7), (8, 7), (7, 7)]
    interpolate_backwards = interpolate_points((9, 7), (7, 7))
    assert(interpolate_backwards == backwards)

    vertical = [(4, 5), (4, 6), (4, 7)]
    interpolate_vertical = interpolate_points((4, 5), (4, 7))
    assert(interpolate_vertical == vertical)

    assert(interpolate_points((1, 3), (3, 1)) is None)

test_interpolate()

def interpolate_points_diag(orig: Tuple, dest: Tuple) -> List[Tuple]:
    """ Returns a list of all the points in between orig and dest, works
    also for diagonal points. """
    ip = interpolate_points(orig, dest)

    if ip:
        return ip

    x_orig, y_orig = orig
    x_dest, y_dest = dest
    
    dir_x = 1 if x_orig < x_dest else -1
    dir_y = 1 if y_orig < y_dest else -1

    return list(zip(range(x_orig, x_dest + dir_x, dir_x), range(y_orig, y_dest + dir_y, dir_y)))

def test_interpolate_diag():
    diagonal1 = [(1, 1), (2, 2), (3, 3)]
    interpolate_diagonal1 = interpolate_points_diag((1, 1), (3, 3))
    assert(interpolate_diagonal1 == diagonal1)

    diagonal2 = [(9, 7), (8, 8), (7, 9)]
    interpolate_diagonal2 = interpolate_points_diag((9, 7), (7, 9))
    assert(interpolate_diagonal2 == diagonal2)

test_interpolate_diag()

# part 1
n = 1000
grid = [[0] * n for i in range(n)] # list of lists

for v in values:
    orig, dest = v
    points = interpolate_points(orig, dest)

    if not points:
        continue

    for p in points:
        x, y = p
        grid[y][x] += 1

total = sum([len([e for e in l if e > 1]) for l in grid])
print(total)

# part 2
n = 1000
grid = [[0] * n for i in range(n)] # list of lists

for v in values:
    orig, dest = v
    points = interpolate_points_diag(orig, dest)

    for p in points:
        x, y = p
        grid[y][x] += 1

total = sum([len([e for e in l if e > 1]) for l in grid])
print(total)