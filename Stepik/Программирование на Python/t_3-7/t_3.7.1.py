n = int(input())
res = {}
for i in range(n):
    game = input().split(';')

    t1 = game[0]
    t2 = game[2]

    if t1 not in res:
        res[t1] = [0,0,0,0,0]
    if t2 not in res:
        res[t2] = [0,0,0,0,0]


    res[t1][0] += 1
    res[t2][0] += 1
    score1 = int(game[1])
    score2 = int(game[3])


    if score1 > score2:
        res[t1][1] += 1
        res[t1][4] += 3
        res[t2][3] += 1
    elif score1 == score2:
        res[t1][2] += 1
        res[t2][2] += 1
        res[t1][4] += 1
        res[t2][4] += 1
    else:
        res[t1][3] += 1
        res[t2][1] += 1
        res[t2][4] += 3

for i in res:
    print(i+":"+str(res[i][0]), res[i][1], res[i][2], res[i][3], res[i][4])
