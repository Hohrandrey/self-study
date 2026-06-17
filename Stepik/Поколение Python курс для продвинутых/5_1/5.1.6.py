n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

comp = set(i + 1 for i in range(n))

res = 'YES'
for i in range(n):
    row = sorted(m[i])
    col = sorted(m[j][i] for j in range(n))
    if row != comp or col != comp:
        flag = 'NO'
        break

print(res)