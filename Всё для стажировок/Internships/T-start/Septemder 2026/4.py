#Изучить
"""
6 4
"""


def solve():
    n, k = map(int, input().split())

    lo, hi = 1, n
    result = []

    for i in range(n):
        m = hi - lo + 1
        max_inv = m - 1
        if k >= max_inv:
            result.append(hi)
            hi -= 1
            k -= max_inv
        else:
            result.append(lo + k)
            for j in range(lo, hi + 1):
                if j != lo + k:
                    result.append(j)
            break

    print(' '.join(map(str, result)))


solve()