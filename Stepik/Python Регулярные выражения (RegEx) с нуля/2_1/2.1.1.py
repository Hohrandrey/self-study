import re

sub_str = r"Apple"
string = input()

if re.match(sub_str, string):
    print("Found")
else:
    print("Not found")
