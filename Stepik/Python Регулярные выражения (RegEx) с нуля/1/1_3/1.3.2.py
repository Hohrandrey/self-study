import re

string = input()
https = r"https"

if re.match(https, string):
    print("Secure")
else:
    print("Insecure")
