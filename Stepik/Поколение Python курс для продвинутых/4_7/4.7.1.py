A = [[1,1,1], [2,2,2], [3,3,3]]
B = [[1,2,3], [4,5,6], [7,8,9]]
res = [[0 for _ in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        res[i][j] = A[i][j] + B[i][j]

for line in res:
    print(*line)