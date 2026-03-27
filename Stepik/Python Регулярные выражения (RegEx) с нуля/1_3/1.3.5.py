import re

string = input()
sub_str = r"\["

if re.match(sub_str, string):
    print("Bracket found")
else:
    print("No bracket at start")