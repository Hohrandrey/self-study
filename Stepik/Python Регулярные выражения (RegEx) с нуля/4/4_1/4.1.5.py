import re

string = input()
sub_str = r"System"
res = re.findall(sub_str, string)

if res:
    print(len(res))
else:
    print("System clean")
