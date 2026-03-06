import requests

file = requests.get('https://stepik.org/media/attachments/course67/3.6.2/008.txt'.strip())
text = list(file.text.splitlines())

print(len(text))