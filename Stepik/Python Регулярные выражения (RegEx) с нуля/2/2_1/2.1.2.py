import re

sub_str = r"b.d"
string = input()
res = re.match(sub_str, string)

if res:
    print(res.group())
else:
    print("No match")
