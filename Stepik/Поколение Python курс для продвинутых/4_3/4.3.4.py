from math import factorial


n_max = int(input())

res = []

for n in range(0, n_max):
    m = 0
    line = []
    while m <= n:
        cur_int = (factorial(n))/(factorial(m)*factorial(n-m))
        m += 1
        line.append(int(cur_int))
    res.append(line)

for line in res:
    print(*line)