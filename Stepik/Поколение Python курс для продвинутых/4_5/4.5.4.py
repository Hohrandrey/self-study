n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and flag:
            flag = False

if flag:
    print("YES")
else:
    print("NO")