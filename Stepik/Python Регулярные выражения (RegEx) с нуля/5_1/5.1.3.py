import re

string = input()
sub_str = r"Item: (\w+)"

print(re.findall(sub_str, string))
