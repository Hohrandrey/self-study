import re

string = input()
sub_str = r"#\w+"
res = re.findall(sub_str, string)

print(res)
