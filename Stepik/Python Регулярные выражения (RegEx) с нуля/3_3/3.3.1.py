import re

string = input()
sub_str = r"\d{4}"

if re.fullmatch(sub_str, string):
    print("Valid PIN")
else:
    print("Invalid PIN")