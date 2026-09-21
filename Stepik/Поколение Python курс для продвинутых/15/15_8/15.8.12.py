from functools import reduce

an = list(map(int, input().split()))
x = int(input())


def evaluate(coefficients, x):
    indexes = [i for i in range(len(coefficients))][::-1]
    print(
        reduce(lambda a, b: a + b, map(lambda a, i: a * x**i, coefficients, indexes), 0)
    )


evaluate(an, x)
