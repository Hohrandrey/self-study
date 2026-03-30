import re

string = input()
syb_str = r"Log"
res = re.match(syb_str,string)

if res:
    end = res.end()
    print(string[end:])
else:
    print()