import re

string = input()
res = re.match(r"[mM]oscow", string)

if res:
    print("Found")
else:
    print("Not found")