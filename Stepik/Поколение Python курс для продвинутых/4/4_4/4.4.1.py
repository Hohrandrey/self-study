n = int(input())
m = int(input())

sp = []
for i in range(n):
    sp.append([])
    for j in range(m):
        sp[i].append(input())


for i in range(n):
    for j in range(m):
        print(sp[i][j], end=" ")
    print()
