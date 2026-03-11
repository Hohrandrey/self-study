mass = float(input())
height = float(input())

imt = mass/height**2

if 18.5 <= imt <= 25:
    print("Оптимальная масса")
elif imt < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")