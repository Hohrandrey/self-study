from fractions import Fraction

numbers = ['3.1415', '-2.8', '4.123', '7.856']
fraction_nums = [Fraction(i) for i in numbers]
for i in range(len(fraction_nums)):
    print(f'{numbers[i]} = {fraction_nums[i]}')