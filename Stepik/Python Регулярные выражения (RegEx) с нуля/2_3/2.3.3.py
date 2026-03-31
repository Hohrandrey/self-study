import re

string = input()
sub_str = r"\w"
res = re.match(sub_str, string)

if res:
    print("Valid start")
else:
    print("Invalid start")