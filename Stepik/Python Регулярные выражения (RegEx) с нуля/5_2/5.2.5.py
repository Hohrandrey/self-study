import re

string = input()
sub_str = r"(?P<first>\w)(.*)(?P=first)"

res = re.match(sub_str, string)
if res:
    print("Same letter")
else:
    print("Different")