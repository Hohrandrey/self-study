import re

string = input()
sub_str = r"/start"

if re.match(sub_str, string):
    print("Command recognized")
else:
    print("Text message")