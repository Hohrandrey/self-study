import re

string = input()
sub_str = r"(\d{4})-(\d{2})-(\d{2})"
res = re.search(sub_str, string)

if res:
    print(f"Year: {res.group(1)}\nMonth: {res.group(2)}\nDay: {res.group(3)}")
else:
    print("Wrong format")
