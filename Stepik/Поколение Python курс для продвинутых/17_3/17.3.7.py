import random

def generate_name(f, l):
    with open(f, 'r', encoding='utf-8') as first, open(l, 'r', encoding='utf-8') as last:
        f = first.readlines()
        l = last.readlines()

    return f'{random.choice(f).strip()} {random.choice(l).strip()}'

print(generate_name('f_7.txt', 'l_7.txt'))