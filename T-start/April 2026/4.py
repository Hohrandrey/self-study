def solve_task4():
    n = int(input())
    p = list(map(int, input().split()))

    if n < 2:
        return 0

    left_profit = [0] * n
    min_price = p[0]
    for i in range(1, n):
        min_price = min(min_price, p[i])
        profit = p[i] - min_price
        left_profit[i] = max(left_profit[i - 1], profit)

    right_profit = [0] * n
    max_price = p[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, p[i])
        profit = max_price - p[i]
        right_profit[i] = max(right_profit[i + 1], profit)

    result = 0
    for i in range(n):
        result = max(result, left_profit[i] + right_profit[i])
    return result

print(solve_task4())