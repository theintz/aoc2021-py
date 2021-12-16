with open("day13-input.txt") as f:
    values = f.read().splitlines()
    coords = [tuple(v.split(",")) for v in values if not v.startswith("fold") and v != ""]
    coords = [(int(x), int(y)) for x, y in coords]
    folds = [tuple(v[11:].split("=")) for v in values if v.startswith("fold")]
    folds = [(dir, int(n)) for dir, n in folds]

# part 1
fold_dir, fold_n = folds[0]

new_coords = set([(x if x < fold_n or fold_dir == "y" else abs(x - 2 * fold_n), \
    y if y < fold_n or fold_dir == "x" else abs(y - 2 * fold_n)) for x, y in coords])

print(len(new_coords))

# part 2
for fold_dir, fold_n in folds:
    coords = set([(x if x < fold_n or fold_dir == "y" else abs(x - 2 * fold_n), \
        y if y < fold_n or fold_dir == "x" else abs(y - 2 * fold_n)) for x, y in coords])
    
    print(len(coords))

for y in range(6):
    for x in range(40):
        print("X" if (x, y) in coords else ".", end="")
    
    print()
