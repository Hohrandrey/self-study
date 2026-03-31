import re

string = input()
sub_str = r"\d\d:\d\d"
res = re.match(sub_str, string)

if res:
    print("Time found")
else:
    print("Not a time")