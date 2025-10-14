start_matr = []


while True:
    line = input().strip()
    if line == "end":
        break
    row = list(map(int, line.split()))
    start_matr.append(row)

rows = len(start_matr)
colums = len(start_matr[0])

res_matr = [[0 for i in range(colums)] for j in range(rows)]


for i in range(rows):
    for j in range(colums):
        print((i - 1) % rows)
        print((i + 1) % rows)
        top = start_matr[(i - 1) % rows][j]
        bottom = start_matr[(i + 1) % rows][j]
        left = start_matr[i][(j - 1) % colums]
        right = start_matr[i][(j + 1) % colums]
        res_matr[i][j] = top + bottom + left + right

for row in res_matr:
    print(' '.join(map(str, row)))