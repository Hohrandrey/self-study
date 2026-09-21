import re

string = input()
rule = r"yes"

result = re.sub(rule, "no", string, count=2)
print(result)
