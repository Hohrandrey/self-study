n = int(input())

players = {}

for _ in range(n):
    players[input()] = 0


m = int(input())
sc_1 = 0
sc_2 = 0
for i in range(m):
    score = input().split()
    new_score = score[0].split(':')
    n_sc_1 = int(new_score[0])
    n_sc_2 = int(new_score[1])
    if n_sc_1 > sc_1:
        players[score[1]] += (n_sc_1 - sc_1)
    elif n_sc_2 > sc_2:
        players[score[1]] += (n_sc_2 - sc_2)
    sc_1 = n_sc_1
    sc_2 = n_sc_2

max_score = max(players.values())

winner = [name for name, score in players.items() if score == max_score][0]

print(winner, max_score)