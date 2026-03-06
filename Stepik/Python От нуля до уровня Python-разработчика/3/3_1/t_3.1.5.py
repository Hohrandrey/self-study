income = int(input())

if income > 50000:
    tax = income * 0.3
elif 50000 >= income >= 10000:
    tax = income * 0.2
else:
    tax = income * 0.1

print(f'Ваш налог: {tax}')