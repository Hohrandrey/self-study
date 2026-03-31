import re

string = input()
sub_str = r"\s"
res = re.match(sub_str, string)

if res:
    print("Indented")
else:
    print("No indentation")