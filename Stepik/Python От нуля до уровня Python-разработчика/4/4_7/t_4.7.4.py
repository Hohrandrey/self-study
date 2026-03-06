def read_and_divide():
    first = int(input())
    second = int(input())
    if second == 0:
        raise ZeroDivisionError
    elif type(first) not in [int, float] or type(second) not in [int, float]:
        raise ValueError
    else:
        return first / second


def task6():
    try:
        res = read_and_divide()
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except ValueError:
        print("Ошибка: некорректное значение")
    else:
        print(f"Результат: {res}")


task6()
