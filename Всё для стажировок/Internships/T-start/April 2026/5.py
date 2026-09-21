def solve_task5():
    n = int(input())
    s = input()

    VALID = {"T", "O", "I"}

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0 if s[i] in VALID else 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            val = 1 + dp[i + 1][j]

            val = min(val, 1 + dp[i][j - 1])

            inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0

            for c in VALID:
                cost_i = 0 if s[i] == c else 1
                cost_j = 0 if s[j] == c else 1
                val = min(val, cost_i + cost_j + inner)

            dp[i][j] = val

    print(dp[0][n - 1])


solve_task5()
