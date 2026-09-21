import re

string = input()
sub_str = r"\w{5,}"
res = re.findall(sub_str, string)

print(res)
