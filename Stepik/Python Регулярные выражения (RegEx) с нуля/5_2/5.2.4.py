import re

string = input()
sub_str = r"(?P<first>\w+), (?P<last>\w+)"
replacement = r"\g<last> \g<first>"

res = re.sub(sub_str, replacement, string)
if res:
    print(res)
else:
    print(string)
