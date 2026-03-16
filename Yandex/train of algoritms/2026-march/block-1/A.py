p, v = map(int, input().split())
q, m = map(int, input().split())
"""
не макс бал

obsh = {p, q}
for i in range(v):
    obsh.add(p + (i + 1))
    obsh.add(p - (i + 1))

for i in range(m):
    obsh.add(q + (i + 1))
    obsh.add(q - (i + 1))

print(len(obsh))
"""

