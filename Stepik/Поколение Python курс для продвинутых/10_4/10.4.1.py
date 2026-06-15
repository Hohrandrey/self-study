dic = {}
for _ in range(int(input())):
    item = input().split(": ")
    dic[item[0].lower()] = item[1]

req = []
for _ in range(int(input())):
    req.append(input())

for item in req:
    item = item.lower()
    print(dic.get(item, 'Не найдено'))