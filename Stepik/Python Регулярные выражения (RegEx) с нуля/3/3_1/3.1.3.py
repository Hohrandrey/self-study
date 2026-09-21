import re

string = input()
sub_string = r"PASS"

if re.fullmatch(sub_string, string):
    print("Access granted")
else:
    print("Access denied")
