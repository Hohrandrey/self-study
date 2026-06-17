n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

degree = int(input())
sec_matrix = [row[:] for row in matrix]

for _ in range(degree-1):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += sec_matrix[i][k] * matrix[k][j]
    sec_matrix = [row[:] for row in temp]

for elem in sec_matrix:
    print(*elem)