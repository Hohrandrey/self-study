spendings = [
    ('аптека', 1300), ('пекарня', 350),
    ('проезд в автобусе', 43),
    ('ресторан', 2300), ('кофейня', 300),
    ('аптека', 2900), ('зоотовары', 750),
    ('кофейня', 290), ('ресторан', 3540),
    ('проезд в автобусе', 43),
    ('такси', 540), ('кино', 880),
]


def show_top_categories(spendings, num):
    ans = {}
    for category, amount in spendings:
        ans[category] = ans.get(category, 0) + amount
    ans = sorted(ans, key=ans.get, reverse=True)[:num]
    print(*sorted(ans), sep='\n')

show_top_categories(spendings, 4)