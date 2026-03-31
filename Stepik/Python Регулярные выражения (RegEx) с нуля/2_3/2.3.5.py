import re

string = input()
sub_str = r"\W"
res = re.match(sub_str, string)

if res:
    print("Special symbol")
else:
    print("Word char")