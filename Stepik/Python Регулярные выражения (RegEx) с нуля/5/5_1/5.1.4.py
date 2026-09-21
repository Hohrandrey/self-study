import re

string = input()
sub_str = r"((\d+),\s*(\d+))"
res = re.search(sub_str, string)

print(f"Full: {res.group(1)} | X: {res.group(2)} | Y: {res.group(3)}")
