n = int(input())
flag = True
matrix = []


for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)


sum_line = sum(matrix[0])
osnov_diag = 0
vtor_diag = 0


for i in range(n):
    sum_table = 0
    osnov_diag += matrix[i][i]
    vtor_diag += matrix[n-1-i][i]
    if sum(matrix[i]) != sum_line:
        flag = False
    for j in range(n):
        sum_table += matrix[j][i]
    if sum_table != sum_line:
        flag = False


if osnov_diag != sum_line or vtor_diag != sum_line:
    flag = False


res_list = []
for line in matrix:
    res_list.extend(line)


for i in range(n**2):
    if i+1 not in res_list:
        flag = False


if flag:
    print("YES")
else:
    print("NO")