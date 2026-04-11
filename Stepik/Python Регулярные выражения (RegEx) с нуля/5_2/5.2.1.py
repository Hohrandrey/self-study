import re

string = input()
sub_str = r"(?P<title>\w+\s\w+) \((?P<year>\d+)\)"

if re.match(sub_str, string):
    print("Title:", re.match(sub_str, string).group("title"))
    print(f"Year: {re.match(sub_str, string).group("year")}")
else:
    print("Error")