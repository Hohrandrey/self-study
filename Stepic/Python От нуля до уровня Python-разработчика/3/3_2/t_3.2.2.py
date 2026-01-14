n = int(input())
count = 0

if  n > 1:
    for i in range(2, int((n**0.5)+1)):
        if n % i == 0:
            count += 1

if count >= 1 or n <=1:
    print(f'{n} не является простым числом')
else:
    print(f'{n} является простым числом')
