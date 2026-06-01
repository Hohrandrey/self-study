n,m=map(int,input().split())
matrix=[[0] * m for _ in range(n)]

num=0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                num+=1
                matrix[i][j]=num

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()