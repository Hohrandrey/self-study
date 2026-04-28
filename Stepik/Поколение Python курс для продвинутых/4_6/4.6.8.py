n, m = map(int, input().split())

matrix = []

for i in range(n):
    line = []
    for j in range(m):
        line.append(i*m+j+1)
    if i % 2 == 0:
        matrix.append(line)
    else:
        matrix.append(line[::-1])

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = '')
    print()