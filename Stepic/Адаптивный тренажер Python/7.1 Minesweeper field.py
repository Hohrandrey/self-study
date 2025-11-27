n, m  = map(int, input().split())

matrics = []

for _ in range(n):
    matrics.append(list(input()))

res_matrix = matrics

for i in range(n):
    for j in range(m):
        if matrics[i][j] == '*':
            res_matrix[i][j] = '*'
        else:
            res_matrix[i][j] = '1'


print(res_matrix)