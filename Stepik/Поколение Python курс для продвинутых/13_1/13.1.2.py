from decimal import *

s = '12.3 1.8 3.6 -1.2 0.5 -14.2 86.5 10.3'
sp = [Decimal(i) for i in s.split()]
print(sum(sp))
print(*sorted(sp, reverse=True)[:5])