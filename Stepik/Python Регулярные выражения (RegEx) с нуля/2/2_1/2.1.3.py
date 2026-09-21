import re

sub_str = r"1..1"
string = input()
res = re.match(sub_str, string)

if res:
    print("Match")
else:
    print("No match")
