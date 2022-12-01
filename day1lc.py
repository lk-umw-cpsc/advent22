
with open('1.txt') as f:
    lines = [line.strip() for line in f]
    newlines = [i for i, line in enumerate(lines) if line == '']
    elves = [sub for sub in [lines[i+1:j] for i, j in zip([-1]+newlines, newlines)]]
    sums = [sum(l) for l in [[int(cal) for cal in elf] for elf in elves]]
    sums.sort(reverse=True)
    print('Part 1:')
    print(sums[0])
    print('Part 2:')
    print(sum(sums[:3]))