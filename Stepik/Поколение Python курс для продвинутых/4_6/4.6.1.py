n, m = map(int, input().split())

matrix = []

for i in range(n):
    line = []
    for j in range(m):
        if (i+j) % 2 == 0:
            line.append(".")
        else:
            line.append("*")
    matrix.append(line)

for line in matrix:
    print(*line)