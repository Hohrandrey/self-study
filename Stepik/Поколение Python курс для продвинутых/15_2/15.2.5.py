

def print_products(*args):
    c = 0
    for item in args:
        if type(item) == str and len(item) > 0:
            c = c + 1
            print(f'{c}) {item}')
    if not c:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')