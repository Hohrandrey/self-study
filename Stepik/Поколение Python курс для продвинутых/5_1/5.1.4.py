n = int(input())
m = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n//2) or (j == n//2) or (i == n-1-j):
            m[i][j] = '*'

for line in m:
    print(*line)