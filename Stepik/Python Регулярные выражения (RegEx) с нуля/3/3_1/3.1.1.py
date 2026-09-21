import re

string = input()
sub_str = r"^Error"

if re.search(sub_str, string):
    print("Log Error")
else:
    print("Log Info")
