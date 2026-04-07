import re

string = input()
res = re.match(r"[+.,-]", string)

if res:
    print("Symbol found")
else:
    print("No symbol")
