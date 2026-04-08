import re

string = input()

sub_str = r"C:\\"

if re.match(sub_str, string):
    print("Disk C")
else:
    print("Other")
