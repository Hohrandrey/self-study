n = int(input())

chetverti = [0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, input().split())
    if x < 0 < y:
        chetverti[1] += 1
    elif x > 0 and y > 0:
        chetverti[0] += 1
    elif x < 0 and y < 0:
        chetverti[2] += 1
    elif x > 0 > y:
        chetverti[3] += 1

print(f"Первая четверть: {chetverti[0]}")
print(f"Вторая четверть: {chetverti[1]}")
print(f"Третья четверть: {chetverti[2]}")
print(f"Четвертая четверть: {chetverti[3]}")
