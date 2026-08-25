import math


def square(num):
    return num*num
def cube(num):
    return num*num*num
def root(num):
    return num**0.5

dict_of_funcs = {'квадрат': square, 'куб': cube, 'корень':root, 'модуль':abs, 'синус':math.sin}

n = int(input())
func_name = input()
print(dict_of_funcs[func_name](n))