dic = {}

line = input().split()
res = []
for el in line:
    num = dic.get(el, 0)
    if num == 0:
        res.append(el)
    else:
        res.append(el+f'_{num}')
    dic[el] = num + 1

print(*res)