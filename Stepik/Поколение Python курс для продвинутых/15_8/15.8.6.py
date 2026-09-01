numbers = [5, 46, 47, 8, 12, 95, 32]

fil_nums = filter(lambda num: not (num % 2 == 1 and num > 47), numbers)
maped_nums = map(lambda x: x//2 if x % 2 == 0 else x, fil_nums)
print(*maped_nums)