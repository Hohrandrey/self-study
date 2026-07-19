from fractions import Fraction
from decimal import Decimal

s = '0.21 74.5 12.3 -11.77 48.6542 114.55'
decimal_sp  = [Decimal(i) for i in s.split()]
print(Fraction(min(decimal_sp)+max(decimal_sp)))