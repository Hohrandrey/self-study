dict_des = {}
dict_kub = {}
dict_pol = {}

res_dict = {'Десяточка' : [], 'Кубит' : [], 'Полоса' : []}

with open('desyatochka.txt', encoding='utf-8') as d:
    for line in d:
        line = line.strip().split(': ')
        dict_des[line[0]] = line[1]

with open('kubit.txt', encoding='utf-8') as k:
    for line in k:
        line = line.strip().split(': ')
        dict_kub[line[0]] = line[1]

with open('polosa.txt', encoding='utf-8') as p:
    for line in p:
        line = line.strip().split(': ')
        dict_pol[line[0]] = line[1]


n = int(input())
list_shop = [input() for i in range(n)]

for item in list_shop:
    cur = []
    if item in dict_des:
        cur.append(('Десяточка', dict_des[item]))
    if item in dict_kub:
        cur.append(('Кубит', dict_kub[item]))
    if item in dict_pol:
        cur.append(('Полоса', dict_pol[item]))

    minimum = min(cur, key=lambda x: int(x[1]))
    res_dict[minimum[0]].append(item)

for key, value in res_dict.items():
    print(f'{key}:')
    if value == []:
        print('–')
    else:
        print(*value,sep=', ')