import re

string = input()
sub_str = r"\send$"

if re.search(sub_str, string):
    print("Match")
else:
    print("No match")
