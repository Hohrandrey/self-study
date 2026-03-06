s = 0
res = []
while True:
    i = int(input())
    s += i
    res.append(i*i)
    if s == 0:
        break
print(sum(res))