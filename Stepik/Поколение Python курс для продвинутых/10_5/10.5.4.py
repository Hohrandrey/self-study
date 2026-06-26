data1 = {'a': 5, 'b': 6, 'c': 7, 'd': 8}
data2 = {'a': 5, 'd': 8}
data3 = {'a': 15, 'b': 6, 'c': 3}
data4 = {'b': 6, 'c': 8}

def dict_diff(data1, data2):
    res_dic = {}
    for elem in data1:
        if elem not in data2:
            res_dic[elem] = 'deleted'
        else:
            if data1[elem] != data2[elem]:
                res_dic[elem] = 'changed'
            else:
                res_dic[elem] = 'unchanged'
    for elem in data2:
        if elem not in data1:
            res_dic[elem] = 'added'
    return res_dic

print(dict_diff(data1, data2))
print(dict_diff(data2, data3))
print(dict_diff(data3, data4))
print(dict_diff(data4, data1))
print(dict_diff(data2, data1))
print(dict_diff(data4, data3))
print(dict_diff(data1, data3))
print(dict_diff(data4, data2))