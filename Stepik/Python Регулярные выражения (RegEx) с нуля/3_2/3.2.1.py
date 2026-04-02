import re

string = input()
sub_str = r"https?://site.com"

if re.fullmatch(sub_str,string):
    print("Correct protocol")
else:
    print("Wrong format")