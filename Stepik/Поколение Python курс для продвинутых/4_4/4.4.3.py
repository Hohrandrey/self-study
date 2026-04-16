n = int(input())
sp = []
res = 0

for _ in range(n):
    sp.append(input().split())

for i in range(n):
    res += int(sp[i][i])

print(res)