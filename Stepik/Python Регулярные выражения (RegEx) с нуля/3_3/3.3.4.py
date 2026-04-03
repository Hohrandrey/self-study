import re

string = input()
sub_str = r"Z{2,5}"

if re.fullmatch(sub_str, string):
    print("Match")
else:
    print("No match")