a = int(input())
b = int(input())


try:
    res = a / b
except ValueError:
    print("Ошибка: введены некорректные данные")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
else:
    print(f"Результат: {res}")
finally:
    print("Операция завершена")
