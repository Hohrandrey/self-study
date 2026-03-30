import re

string = input()
sub_str = r"error"
res = re.search(sub_str, string)

if res:
    print(f"Start index: {res.start()}")
else:
    print("No error")