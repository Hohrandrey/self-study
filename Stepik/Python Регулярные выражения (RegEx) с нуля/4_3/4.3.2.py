import re

text = open(0).read()

pattern = re.compile(r"\.jpg$")

files = text.splitlines()

for filename in files:
    if pattern.search(filename):
        print(filename)