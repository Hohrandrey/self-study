"""
def func_apply(func, arr):
    s = []
    for el in arr:
        n_s = func(el)
        s.append(n_s)
    return s
"""

def func_apply(func, arr):
    return list(map(func, arr))

print(func_apply(int, ['1', '2', '10']))
print(func_apply(bool, [1, 2, 3, 4, 5, 0]))