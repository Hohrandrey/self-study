n = int(input())
matrix = [["0" for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (j >= i and i <= n - 1 - j) or (i >= n - 1 - j and i >= j):
            matrix[i][j] = "1"
        print(str(matrix[i][j]).ljust(3), end="")
    print()
