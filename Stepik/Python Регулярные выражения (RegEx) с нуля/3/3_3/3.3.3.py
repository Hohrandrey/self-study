import re

string = input()
sub_str = r"\w{6,}"

if re.search(sub_str, string):
    print(re.search(sub_str, string).group())
else:
    print("No long words")
