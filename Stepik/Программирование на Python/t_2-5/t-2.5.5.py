inp = list(map(int, input().split()))

se = set(inp)

res = []

for s in se:
    if inp.count(s) > 1:
        res.append(s)

for r in res:
    print(r, end=' ')