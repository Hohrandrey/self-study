n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

sp = []
for i in range(n):
    for j in range(n):
        if (j >= i >= n-1-j) or (i >= j and i > n - 1 - j):
            sp.append(m[i][j])
print(max(sp))