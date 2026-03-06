lst = input().split()
x  = input()

res  = []

for i in range(len(lst)):
    if lst[i]  == x:
        res.append(str(i))

if len(res) != 0:
    print(' '.join(res))
else:
    print('Отсутствует')