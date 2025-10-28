import numpy as np

n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    inp = input().split()
    for x in range(len(inp)):
        matrix[i][x] = int(inp[x])

# Вариант 1
transposed = [[0 for _ in range(n)] for _ in range(m)]
for j in range(m):
    for i in range(n):
        transposed[j][i] = matrix[i][j]
        print(transposed[j][i], end=' ')
    print()

# вариант 2
matrix = np.array(matrix)
transposed = np.transpose(matrix)
for j in range(m):
    for i in range(n):
        print(transposed[j][i], end = ' ')
    print()