import re

string = input()
res = re.match(r"file\.txt",string)

if res:
    print("Found")
else:
    print("False alarm")