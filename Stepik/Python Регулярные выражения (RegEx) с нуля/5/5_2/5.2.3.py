import re

string = input()
sub_str = r"<(?P<tag>\w+)>(.*?)</(?P=tag)>"

if re.search(sub_str, string):
    print("Valid tag")
else:
    print("Invalid tag")
