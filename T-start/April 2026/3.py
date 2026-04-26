def solve_task3():
    n, m =  map(int, input().split())

    mod = 10 ** 9 + 7

    if n == 1:
        print((m * (m - 1)) % mod)
        return

    first_col = (m * (m - 1)) % mod
    transition = (m * m - 3 * m + 3) % mod

    ans = (first_col * pow(transition, n - 1, mod)) % mod
    print(ans)

solve_task3()