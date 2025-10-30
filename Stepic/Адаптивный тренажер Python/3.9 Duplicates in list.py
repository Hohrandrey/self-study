inp = input().split()
res = []
for elem in inp:
    if inp.count(elem) > 1:
        res.append(elem)

for i in sorted(set(res)):
    print(i)

