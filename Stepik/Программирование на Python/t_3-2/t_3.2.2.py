inp = input().lower().split()
res = {}
for i in set(inp):
    res[i] = inp.count(i)
    print(i, res[i])