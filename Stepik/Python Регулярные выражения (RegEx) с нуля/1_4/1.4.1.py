import re

string = input()
sub_str = r"Python"

if re.match(sub_str, string):
    print(re.match(sub_str, string).group())
else:
    print("Not found")
