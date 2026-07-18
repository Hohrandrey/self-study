product_list = [
    'молоко', 'яйцо', 'колбаса', 'лук',
    'помидор', 'помидор', 'майонез',
    'хлеб', 'лук', 'сливочное масло',
]

def print_product_list(product_list):
    dic = {
    'яблоко': '🍎', 'хлеб': '🍞', 'конфеты': '🍬', 'лимон': '🍋',
    'морковь': '🥕', 'огурец': '🥒', 'помидор': '🍅', 'яйцо': '🥚',
    'чеснок': '🧄', 'авокадо': '🥑', 'спички': '🥢', 'соль': '🧂',
    'филе говядины': '🥩', 'киви': '🥝', 'лук': '🧅', 'сыр': '🧀',
    }
    set_product_list = set(product_list)
    for elem in set_product_list:
        icon = dic.get(elem, elem)
        print(icon+": "+str(product_list.count(elem)))


print_product_list(product_list)
