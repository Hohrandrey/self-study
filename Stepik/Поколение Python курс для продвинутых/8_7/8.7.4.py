s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = set(map(int, input().split()))

two = (s1 & s2 - s3) | (s2 & s3 - s1) | (s1 & s3 - s2)
one = (s1 - s2 - s3) | (s2 - s1 - s3) | (s3 - s1 - s2)
print(*sorted(one|two))