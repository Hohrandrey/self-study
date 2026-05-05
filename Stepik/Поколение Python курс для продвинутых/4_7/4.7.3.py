A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]


for row in C:
    print(*row)