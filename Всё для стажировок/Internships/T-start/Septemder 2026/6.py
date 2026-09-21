"""
3
1 3 1
1 5 1
2 2 1
4 2 0
1 5 4
5 1 3
1 2 1
3 3 4
"""
#Изучить

n = int(input())

num = 1 << n

c = []
for i in range(num):
    row = list(map(int, input().split()))
    c.append(row)

dp = [[0] * (n + 1) for _ in range(1 << (n + 1))]

for i in range(num):
    v = (1 << n) + i
    for k in range(1, n + 1):
        dp[v][k] = c[i][k - 1]

for h in range(1, n + 1):
    start = 1 << (n - h)
    end = 1 << (n - h + 1)
    for v in range(start, end):
        l, r = 2 * v, 2 * v + 1
        dl0, dr0 = dp[l][0], dp[r][0]
        for k in range(n - h + 1):
            dp[v][k] = max(dp[l][1 + k] + dr0, dp[r][1 + k] + dl0)

print(dp[1][0])
