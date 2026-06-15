dict_of_countries = {}

for _ in range(int(input())):
    country, *towns = input().split()
    dict_of_countries[country] = towns

res_ans = []
for _ in range(int(input())):
    z = input()
    for key, value in dict_of_countries.items():
        if z in value:
            res_ans.append(key)

print(*res_ans, sep='\n')