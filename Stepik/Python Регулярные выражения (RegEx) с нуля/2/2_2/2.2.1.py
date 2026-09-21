import re

string = input()

if re.match(r"[aeiou]", string):
    print("Vowel")
else:
    print("Consonant")
