A = [[1, -1, 0], [3, -4, 2]]
B = [[1, 2], [3, 4], [5, 6]]

C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

print(C)

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]


for row in C:
    print(*row)
