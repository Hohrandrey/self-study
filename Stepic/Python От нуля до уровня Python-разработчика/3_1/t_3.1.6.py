time = int(input())

if 6 <= time <= 11:
    res = 'Доброе утро!'
elif 12 <= time <= 17:
    res = 'Добрый день!'
elif 18 <= time <= 21:
    res = 'Добрый вечер!'
else:
    res = 'Доброй ночи!'

print(res)
