age = int(input())

if age < 0:
    print('Ошибка')
elif 0 <= age <= 17:
    print('Детство')
elif 18 <= age <= 64:
    print('Взрослый')
else:
    print('Пенсионер')
