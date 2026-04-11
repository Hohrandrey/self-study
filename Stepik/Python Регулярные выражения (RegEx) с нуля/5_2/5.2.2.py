import re

string = input()
sub_str = r"(\w+) \1"

if re.match(sub_str, string):
    print(re.match(sub_str, string).group(1))
else:
    print("No duplicates")