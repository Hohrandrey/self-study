dic = {}
for i in range(int(input())):
    name, product, count = input().split()
    dic[name] = dic.get(name, {})
    dic[name][product] = dic[name].get(product, 0) + int(count)


for name in sorted(dic):
    print(f'{name}:')
    for product in sorted(dic[name]):
        print(f'{product} {dic[name][product]}')