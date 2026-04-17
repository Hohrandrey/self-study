n = int(input())
sp = []

for _ in range(n):
    val = list(map(int, input().split()))
    avg = sum(val) / n
    c = 0
    for elem in val:
        if elem > avg:
            c += 1
    sp.append(c)

print(*sp, sep="\n")
