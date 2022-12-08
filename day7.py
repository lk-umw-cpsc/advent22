root = {}
with open('7.txt') as f:
    curdir = root
    f.readline()
    for line in f:
        line = line.strip()
        if line.startswith('$'):
            args = line.split()[1:]
            if args[0] == 'cd':
                curdir = curdir[args[1]]
        else:
            info = line.split()
            typ, name = info
            if typ == 'dir':
                directory = { '..' : curdir }
                curdir[name] = directory
            else:
                curdir[name] = int(typ)
global sum
sum = 0

localsums = []
def recur(dir):
    localsum = 0
    for key, value in dir.items():
        if key == '..':
            continue
        if isinstance(value, int):
            localsum += value
        else:
            localsum += recur(value)
    if localsum <= 100000:
        global sum
        sum += localsum
    localsums.append(localsum)
    return localsum

total = recur(root)
localsums.sort()
req = 30000000 - (70000000 - total)
print('req free space', req)
print('Part 1:', sum)
for localsum in localsums:
    if localsum >= req:
        print('Part 2:', localsum)
        break