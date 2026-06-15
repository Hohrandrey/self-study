dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
for key, value in dict2.items():
    if key in dict1:
        dict1[key] = dict1[key] + value
    else:
        dict1[key] = value
print(dict1)