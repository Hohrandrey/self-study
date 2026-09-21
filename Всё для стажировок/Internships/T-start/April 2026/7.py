def solve_task7():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    def count_coins(S):
        cnt = 0
        for i in range(n - 1, -1, -1):
            if S >= a[i]:
                c = S // a[i]
                cnt += c
                S -= c * a[i]
        return cnt

    candidates = set()

    for i in range(n):
        remainder = x % a[i]
        if remainder != 0:
            y_candidate = x + (a[i] - remainder)
            candidates.add(y_candidate)
        else:
            candidates.add(x)

    ans = float("inf")
    for y in candidates:
        if y < x:
            continue
        z = y - x
        c1 = count_coins(y)
        c2 = count_coins(z)
        if c1 + c2 < ans:
            ans = c1 + c2

    print(ans)


solve_task7()
