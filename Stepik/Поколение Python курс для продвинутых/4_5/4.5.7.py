n = int(input())

matrix = []
res_matrix = [[0 for _ in range(n)]for _ in range(n)]

for _ in range(n):
    matrix.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        res_matrix[j][n-1-i] = matrix[i][j]

for line in res_matrix:
    print(*line)