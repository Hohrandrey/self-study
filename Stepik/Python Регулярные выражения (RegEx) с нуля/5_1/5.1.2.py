import re


string = input()
sub_str = r"(ha){2,}"
res = re.fullmatch(sub_str,string)

if res:
    print("Laugh")
else:
    print("Not laugh")
