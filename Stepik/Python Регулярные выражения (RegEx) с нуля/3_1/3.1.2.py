import re

string = input()
sub_string = r"\.png$"

if re.search(sub_string, string):
    print("Image")
else:
    print("Not image")