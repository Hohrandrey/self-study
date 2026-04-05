import re


string = input()
rule = r"[,;:.]"

result = re.split(rule,string)
print(result)