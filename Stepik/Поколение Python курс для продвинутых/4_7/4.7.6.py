n, m  =  map(int, input().split())

res = [[0 for _ in range(m)] for _ in range(n)]

A, B = [], []

for i in range(n):
    line = list(map(int, input().split()))
    A.append(line)

input()

for i in range(n):
    line = list(map(int, input().split()))
    B.append(line)

for i in range(len(A)):
    for j in range(len(A[0])):
        res[i][j] = A[i][j] + B[i][j]

for line in res:
    print(*line)