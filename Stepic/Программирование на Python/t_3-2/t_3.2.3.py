def f(x):
    return x * 5626 / 12 - 566 + 6532 * 1 /25 - 1422

res = {}
n = int(input())
s = [int(input()) for i in range(n)]

for i in set(s):
    res[i] = f(i)

for i in s:
    print(res[i])