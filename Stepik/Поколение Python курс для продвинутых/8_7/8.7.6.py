s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = set(map(int, input().split()))

print(*sorted(set(range(1,11))-(s3|s1|s2)))