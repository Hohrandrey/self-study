def sq_sum(*args):
    return sum(map(lambda x: x * x, args))


print(sq_sum(1, 2, 3))
print(sq_sum(1.5, 2.5))
