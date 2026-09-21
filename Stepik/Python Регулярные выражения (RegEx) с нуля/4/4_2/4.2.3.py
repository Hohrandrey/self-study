import re

string = input()
rule = r"\d"

result = re.sub(rule, "X", string)
print(result)
