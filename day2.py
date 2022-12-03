orock = 'A'
opaper = 'B'
oscissors = 'C'

rock = 'X'
paper = 'Y'
scissors = 'Z'

lose = 'X'
draw = 'Y'
win = 'Z'

p2outcomes = {
    (orock, lose): 3, # 0 + 3
    (orock, draw): 4, # 3 + 1
    (orock, win): 8, # 6 + 2

    (opaper, lose): 1, # 0 + 1
    (opaper, draw): 5, # 3 + 2
    (opaper, win): 9, # 6 + 3

    (oscissors, lose): 2, # 0 + 2 
    (oscissors, draw): 6, # 3 + 3
    (oscissors, win): 7, # 6 + 1
}

choice_scores = {
    rock: 1,
    paper: 2,
    scissors: 3
}

p1matchups = {
    (orock, rock): 3,
    (orock, paper): 6,
    (orock, scissors): 0,
    (opaper, rock): 0,
    (opaper, paper): 3,
    (opaper, scissors): 6,
    (oscissors, rock): 6,
    (oscissors, paper): 0,
    (oscissors, scissors): 3,
}

p1score = 0
p2score = 0

with open('2.txt') as f:
    for line in f:
        line = line.strip()
        opp, me = line.split()
        p1score += choice_scores[me]
        p1score += p1matchups[(opp, me)]
        p2score += p2outcomes[(opp, me)]

print('Part 1:')
print(p1score)
print('Part 2:')
print(p2score)