import re

string = input()
sub_str = r"^\d\d\d$"

if re.search(sub_str,string):
    print("Valid code")
else:
    print("Invalid code")