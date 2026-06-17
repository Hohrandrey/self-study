n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split()))[::-1])

flag = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            flag = False

if flag:
    print('YES')
else:
    print('NO')