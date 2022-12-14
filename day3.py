def priority(c):
    ascii = ord(c)
    if ascii <= ord('Z'):
        return ascii - ord('A') + 27
    return ascii - ord('a') + 1

with open('3.txt') as f:
    input3 = [line.strip() for line in f]
  
p1sum = 0
p2sum = 0
i = 1
for line in input3:
    half = len(line) // 2
    first_half_set = { *line[:half] }
    second_half_set = { *line[half:] }
    item_in_both, = first_half_set.intersection(second_half_set)
    p1sum += priority(item_in_both)
    
    if i == 1:
        badge_set = { *line }
    else:
        rucksack_set = { *line }
        badge_set = badge_set.intersection(rucksack_set)
    if i == 3:
        badge, = badge_set
        p2sum += priority(badge)
    i += 1
    if i > 3:
        i = 1
print('Part 1')
print(p1sum)

print('Part 2')
print(p2sum)