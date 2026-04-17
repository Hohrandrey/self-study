n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


upper, right, lower, left = 0, 0, 0, 0


for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            upper += matrix[i][j]
        elif j > i and j > n - 1 - i:
            right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            lower += matrix[i][j]
        elif j < i and j < n - 1 - i:
            left += matrix[i][j]


print(f"Верхняя четверть: {upper}\nПравая четверть: {right}\nНижняя четверть: {lower}\nЛевая четверть: {left}")
