import re, sys

string = sys.stdin.read()
rule = r"\s+"

result = re.sub(rule, " ", string)
print(result)
