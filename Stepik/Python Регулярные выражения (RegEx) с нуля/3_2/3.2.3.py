import re

string = input()
sub_str = r"be*p"

if re.fullmatch(sub_str, string):
    print("Match")
else:
    print("No match")
