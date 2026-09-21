import re

string = input()
sub_str = r"(\w+)=(\d+)"
res = re.finditer(sub_str, string)

for elem in res:
    print(f"Key: {elem.group(1)}, Value: {elem.group(2)}")
