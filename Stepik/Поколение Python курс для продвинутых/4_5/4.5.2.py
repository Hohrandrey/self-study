n = int(input())
m = int(input())

sp = []
max_val = float("-inf")

for _ in range(n):
    sp.append(list(map(int, input().split())))

for line in sp:
    max_val = max(max(line), max_val)


flag = True
for i in range(n):
    for j in range(m):
        if sp[i][j] == max_val and flag:
            print(i, j)
            flag = False
