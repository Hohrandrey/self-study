import re

sub_str = r"Code"
string = input()

res = re.match(sub_str,string)

if res:
    print(re.match(sub_str,string).span())
else:
    print(None)