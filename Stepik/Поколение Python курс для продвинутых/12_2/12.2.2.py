from random import randint, choice
import string

def generate_index():
    st = string.ascii_uppercase
    return choice(st)+choice(st)+str(randint(0,99))+'_'+str(randint(0,99))+choice(st)+choice(st)

print(generate_index())
print(generate_index())
print(generate_index())