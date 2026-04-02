import re

string = input()
sub_str = r"file\d+"

if re.fullmatch(sub_str,string):
    print("Found ID")
else:
    print("Error")