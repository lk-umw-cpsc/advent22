orock = 'A'
opaper = 'B'
oscissors = 'C'

rock = 'X'
paper = 'Y'
scissors = 'Z'

choice_scores = {
    rock: 1,
    paper: 2,
    scissors: 3
}

matchups = {
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

score = 0

with open('2.txt') as f:
    for line in f:
        line = line.strip()
        opp, me = line.split()
        score += choice_scores[me]
        score += matchups[(opp, me)]
print(score)