n = int(input())
m = int(input())

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j

for i in range(n):
    for j in range(m):
        out = str(matrix[i][j]).ljust(3)
        print(out, end="")
    print()
