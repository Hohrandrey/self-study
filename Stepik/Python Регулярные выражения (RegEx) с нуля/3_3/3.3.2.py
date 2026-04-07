import re

string = input()
sub_str = r"\w{3,10}"

if re.fullmatch(sub_str, string):
    print("OK")
else:
    print("Error")
