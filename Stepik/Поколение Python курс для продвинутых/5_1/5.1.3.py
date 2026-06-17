n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))


m2 = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(m[j][i])
    m2.append(line)

for e in m2:
    print(*e)