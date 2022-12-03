with open('3.txt') as f:
    input3 = [line.strip() for line in f]

def priority(c):
    ascii = ord(c)
    if ascii <= ord('Z'):
        return ascii - ord('A') + 27
    return ascii - ord('a') + 1
    
p1sum = 0
p2sum = 0
i = 1
for line in input3:
    half = len(line) // 2
    first_set = {*line[:half]}
    second_set = {*line[half:]}
    for v in first_set.intersection(second_set):
        p1sum += priority(v)
    
    if i == 1:
        badge_set = { *line }
    else:
        rucksack_set = { *line }
        badge_set = badge_set.intersection(rucksack_set)
    if i == 3:
        for v in badge_set:
            p2sum += priority(v)
    i += 1
    if i > 3:
        i = 1
print('Part 1')
print(p1sum)

print('Part 2')
print(p2sum)