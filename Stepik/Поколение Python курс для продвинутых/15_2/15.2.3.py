
def mean(*args):
    s = 0
    count = 0
    for i in args:
        if type(i) in {int, float}:
            s += i
            count += 1
    if count:
        return s / count
    return 0


print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))