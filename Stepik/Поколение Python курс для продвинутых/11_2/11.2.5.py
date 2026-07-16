def merge(list):
    res = {}
    for dic in list:
        for elem in dic:
           if elem not in res:
               res[elem] = {dic[elem], }
           else:
               res[elem].add(dic[elem])
    return res

print(
    merge(
        [
            {'o': 2, 'k': 4},
            {'x': 1},
            {'p': 2},
            {'k': 2, 'j': 5, 'o': 7},
            {'x': 3, 'k': 4, 'j': 2},
        ]
    )
)