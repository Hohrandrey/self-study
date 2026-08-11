from fractions import Fraction
from math import factorial

n = int(input())
s = 0
for i in range(1, n+1):
    s += Fraction(1, factorial(i))
print(s)