from fractions import Fraction

n = int(input())
s = 0
for i in range(1, n+1):
    s += Fraction(1, i**2)
print(s)