import re

string = input()
sub_str = r"\w{4,}"


res = re.finditer(sub_str, string)


for i in res:
    word = i.group()
    length = len(word)
    index = i.start()
    print(f"Word: {word}, Length: {length}, Start: {index}")
