import re

string = input()
sub_str = r"A{3,7}"

if re.match(sub_str, string):
    print(len(re.match(sub_str, string).group()))
