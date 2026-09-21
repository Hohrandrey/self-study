import re

string = input()
sub_str = r"[^0-9]"
res = re.match(sub_str, string)

if res:
    print("OK")
else:
    print("Error")
