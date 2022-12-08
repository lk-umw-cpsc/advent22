rows = []
with open('8.txt') as f:
    for line in f:
        col = [int(n) for n in line.strip()]
        rows.append(col)
nrows = len(rows)
ncols = len(rows[0])

def scenic(row, col):
    tree = rows[row][col]

    thumb = row - 1
    up = 0
    while thumb >= 0:
        up += 1
        neighbor = rows[thumb][col]
        if neighbor >= tree:
            break
        thumb -= 1
    
    thumb = row + 1
    down = 0
    while thumb  < nrows:
        down += 1
        neighbor = rows[thumb][col]
        if neighbor >= tree:
            break
        thumb += 1

    thumb = col - 1
    left = 0
    while thumb >= 0:
        left += 1
        neighbor = rows[row][thumb]
        if neighbor >= tree:
            break
        thumb -= 1

    thumb = col + 1
    right = 0
    while thumb < ncols:
        right += 1
        neighbor = rows[row][thumb]
        if neighbor >= tree:
            break
        thumb += 1
    return up * down * left * right

best = -1
for r in range(nrows):
    for c in range(ncols):
        s = scenic(r, c)
        if s > best:
            best = s
print(f'Part 2: {best}')