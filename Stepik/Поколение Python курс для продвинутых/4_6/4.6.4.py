n, m = map(int, input().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = n * j + i + 1
        print(str(matrix[i][j]).ljust(3), end="")
    print()
