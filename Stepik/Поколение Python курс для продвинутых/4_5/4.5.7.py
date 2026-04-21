n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]

for line in matrix:
    print(*line)