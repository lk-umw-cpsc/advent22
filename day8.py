rows = []
with open('8.txt') as f:
    for line in f:
        col = [int(n) for n in line.strip()]
        rows.append(col)
nrows = len(rows)
ncols = len(rows[0])
visibilities = []
for i in range(nrows):
    visibilities.append([False] * ncols)

# left to right
for r, row in enumerate(rows):
    row_max = -1
    for c, tree in enumerate(row):
        if tree > row_max and not visibilities[r][c]:
            print(f'{tree} at {r}, {c}')
        v = visibilities[r][c] = tree > row_max
        row_max = max(row_max, tree)
# right to left
for r, row in enumerate(rows):
    row_max = -1
    for c in reversed(range(ncols)):
        tree = rows[r][c]
        if tree > row_max and not visibilities[r][c]:
            print(f'{tree} at {r}, {c}')
        visibilities[r][c] = visibilities[r][c] or tree > row_max
        row_max = max(row_max, tree)
# top to bottom
for c in range(ncols):
    col_max = -1
    for r in range(nrows):
        tree = rows[r][c]
        if tree > col_max and not visibilities[r][c]:
            print(f'{tree} at {r}, {c}')
        visibilities[r][c] = visibilities[r][c] or tree > col_max
        col_max = max(col_max, tree)
        
count = 0
for c in range(ncols):
    col_max = -1
    for r in reversed(range(nrows)):
        tree = rows[r][c]
        if tree > col_max and not visibilities[r][c]:
            print(f'{tree} at {r}, {c}')
        visible = visibilities[r][c] = visibilities[r][c] or tree > col_max
        if visible:
            count += 1
        col_max = max(col_max, tree)

print('Part 1:', count)