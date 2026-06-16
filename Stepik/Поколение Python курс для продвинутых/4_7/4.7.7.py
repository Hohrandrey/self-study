m1 = []
m2 = []


n, m = map(int, input().split())

for i in range(n):
    m1.append(list(map(int, input().split())))

input()

m, k = map(int, input().split())
for i in range(m):
    m2.append(list(map(int, input().split())))

res_m = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            res_m[i][j] += m1[i][x] * m2[x][j]

for row in res_m:
    print(*row)