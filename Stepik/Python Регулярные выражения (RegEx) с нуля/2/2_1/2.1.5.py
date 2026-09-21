import re

string = input()
res = re.match("A.C", string)

if res:
    print("Match")
else:
    print("No match")
