from decimal import *

s = '0.0 5.42 8.63 10.25 1.6 -8.5 -13.0'
sp = [Decimal(elem) for elem in s.split()]
print(max(sp)+min(sp))