n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    c = 0
    for j in range(n):
        if i == j:
            continue
        elif i < j:
            c += 1
            matrix[i][j] = c
        else:
            matrix[i][j] = matrix[j][i]

for row in matrix:
    print(*row)