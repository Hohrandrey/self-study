import re

string =  input()
sub_str = r"RegEx"

if re.match(sub_str, string):
    print("Match")
else:
    print("No match")