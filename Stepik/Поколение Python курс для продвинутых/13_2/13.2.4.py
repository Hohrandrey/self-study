from fractions import Fraction as F

f, s = input(), input()
print(f'{f} + {s} = {F(f)+F(s)}')
print(f'{f} - {s} = {F(f)-F(s)}')
print(f'{f} * {s} = {F(f)*F(s)}')
print(f'{f} / {s} = {F(f)/F(s)}')