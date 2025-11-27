ma = -1
mi = 10
st = input()

for elem in st:
    if int(elem) > ma:
        ma = int(elem)
    if int(elem) < mi:
        mi = int(elem)

print(f'Минимальное число = {mi}, максимальное число = {ma}')