import re

string = input()
sub_str = r"(\d{2}):(\d{2})"
res = re.search(sub_str, string)

if res:
    print(int(res.group(1)) * 60 + int(res.group(2)))
else:
    print("Error")
