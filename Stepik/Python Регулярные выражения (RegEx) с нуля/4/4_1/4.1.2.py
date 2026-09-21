import re

string = input()
sub_str = r"[bB]\w+"
res = re.findall(sub_str, string)

print(res)
