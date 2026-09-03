f = int(input())
s = int(input())

res = []
for i in range(f,s+1):
    cur_del =[]
    for j in str(i):
        cur_del.append(j != '0' and i%int(j)==0)
    if all(cur_del):
        res.append(i)
print(*res)