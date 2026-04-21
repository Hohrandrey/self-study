n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))


for i in range(n//2):
    for j in range(n):
        matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

for line in matrix:
    print(*line)
