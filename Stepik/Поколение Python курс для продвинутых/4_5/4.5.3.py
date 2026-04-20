n = int(input())
m = int(input())

sp = []

for _ in range(n):
    sp.append(list(map(int, input().split())))

i, j = map(int, input().split())

for line in sp:
    line[i], line[j] = line[j], line[i]
    print(*line)
