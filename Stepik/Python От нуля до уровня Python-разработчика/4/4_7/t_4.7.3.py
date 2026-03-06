class NegativeCError(Exception):
    pass


def compute(a, b, c):
    if c < 0:
        raise NegativeCError
    return (a / b) + c ** 0.5


a = int(input())
b = int(input())
c = int(input())
try:
    res = compute(a, b, c)
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
except NegativeCError:
    print("Ошибка: Отрицательный c")
except ValueError:
    print("Ошибка: некорректные данные")
else:
    print(f"Результат: {res}")
finally:
    print("Завершили вычисление")
