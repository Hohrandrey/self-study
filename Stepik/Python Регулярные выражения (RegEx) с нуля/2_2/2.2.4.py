import re

string = input()
res = re.match(r"[A-Z][a-z]", string)

if res:
    print("Match")
else:
    print("No match")