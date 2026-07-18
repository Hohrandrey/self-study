numbers = [1, 6, 18]
print({num : [i for i in range(1, num+1) if num % i == 0] for num in numbers})