numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]


"""

def sum_of_squares(x, y):
    return x + y**2

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc

print(reduce(sum_of_squares, numbers, 0))
"""


def squares(x):
    return x**2


print(sum(map(squares, numbers)))
