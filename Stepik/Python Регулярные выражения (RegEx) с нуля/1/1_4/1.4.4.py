import re

sub_str = r"Key"
string = input()

if re.match(sub_str, string):
    print("Found")
else:
    print("Missing")
