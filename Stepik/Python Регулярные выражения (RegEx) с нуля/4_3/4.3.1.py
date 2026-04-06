import re


string = input()
to_find = r"Python"
res = re.finditer(to_find, string)


for i in res:
    print(f"Found 'Python' at {i.span()}")