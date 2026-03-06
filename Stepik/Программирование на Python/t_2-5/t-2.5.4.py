i = list(map(int, input().split()))

res = []

if len(i) >= 2:
    s = i[1] + i[-1]
    res.append(s)
    for ind in range(1, len(i)-1):
        s = i[ind-1] + i[ind+1]
        res.append(s)
    s = i[-2] + i[0]
    res.append(s)

    for i in res:
        print(i, end=' ')
else:
    for i_ in i:
        print(i_)