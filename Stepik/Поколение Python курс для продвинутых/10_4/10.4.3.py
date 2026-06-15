import re

f = input().lower()
s = input().lower()
f = re.sub(r'[ .,!?:;-]','' , f)
s = re.sub(r'[ .,!?:;-]','' , s)
print('YES' if sorted(f) == sorted(s) else 'NO')
