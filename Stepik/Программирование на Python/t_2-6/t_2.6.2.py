n = int(input())
res = []

for i in range(1, n+1):
    res += [str(i)] * i


print(' '.join(res[:n]))