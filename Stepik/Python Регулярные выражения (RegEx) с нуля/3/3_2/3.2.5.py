import re

string = input()
sub_str = r"Item-?\d+"

if re.fullmatch(sub_str, string):
    print("Valid")
else:
    print("Invalid")
