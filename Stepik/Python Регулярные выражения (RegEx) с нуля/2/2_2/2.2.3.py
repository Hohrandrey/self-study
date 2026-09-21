import re

string = input()
res = re.match(r"[1-5]", string)

if res:
    print("Valid grade")
else:
    print("Invalid grade")
