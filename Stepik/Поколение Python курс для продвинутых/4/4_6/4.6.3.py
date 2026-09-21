n, m = map(int, input().split())

matrix = []
cur_elem = 1

for i in range(n):
    line = []
    for j in range(m):
        line.append(cur_elem)
        cur_elem += 1
    matrix.append(line)


for line in matrix:
    print(*line)
