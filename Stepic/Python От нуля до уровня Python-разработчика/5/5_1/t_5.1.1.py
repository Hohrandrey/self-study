def even_numbers(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num


n = int(input())

even_numbers = even_numbers(n)
for i in even_numbers:
    print(i)
