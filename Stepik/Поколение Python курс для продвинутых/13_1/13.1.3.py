from decimal import *

d = Decimal(input())
d_tup = d.as_tuple().digits
print(max(d_tup)if int(d) == 0 else max(d_tup)+min(d_tup))
