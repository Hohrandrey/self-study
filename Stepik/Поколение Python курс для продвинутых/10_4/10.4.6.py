dic_nums = {}
res = []

for _ in range(int(input())):
    num, name = input().lower().split()
    dic_nums.setdefault(name, []).append(num)


for _ in range(int(input())):
    res.append(dic_nums.get(input().lower(), ['абонент не найден']))

for i in res:
    print(*i)