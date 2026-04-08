import re

sub_str = r"\d+"
iteration = re.finditer(sub_str, input())
s = 0
for i in iteration:
    s += int(i.group())
print(s)
