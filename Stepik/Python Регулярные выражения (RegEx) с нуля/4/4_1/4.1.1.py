import re

string = input()
sub_str = r"\d+"
res = re.findall(sub_str, string)

print(res)
