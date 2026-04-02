import re

string = input()
sub_str = r"No+"

if re.fullmatch(sub_str,string):
    print("Scream")
else:
    print("Quiet")