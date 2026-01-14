su = int(input())
val = input()
if  val == "USD":
    res_su = su / 103
    print(f'{su} RUB = {int(res_su)} {val}')
elif val == "EUR":
    res_su = su / 105
    print(f'{su} RUB = {int(res_su)} {val}')
else:
    print("Неверно указана валюта. Введите 'USD' или 'EUR'")
