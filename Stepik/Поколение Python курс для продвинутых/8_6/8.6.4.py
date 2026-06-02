n = int(input())
s1 = set(input())
for _ in range(n-1):
    s1.intersection_update(set(input()))
print(*sorted(s1))