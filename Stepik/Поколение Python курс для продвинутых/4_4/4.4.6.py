n = int(input())

sp = []
for i in range(n):
    sp.append(list(map(int, input().split())))

max_elem = -10000000000

for i in range(n):
    for j in range(n):
        if j <= i <= n - 1 - j or j >= i >= n - 1 - j:
            max_elem = max(sp[i][j], max_elem)

print(max_elem)
