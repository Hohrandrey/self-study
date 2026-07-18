from random import randint

def coin_flip():
    if randint(0,1) == 0:
        return 'Решка'
    else:
        return 'Орел'