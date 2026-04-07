n = int(input())

lis = []

left_max = -float("inf")
right_min = float("inf")

for i in range(n):
    x, d = map(int, input().split())
    lis.append((x - d, x))
    lis.append((x, x + d))
    left = x - d
    right = x + d
    left_max = max(left_max, left)
    right_min = min(right_min, right)


if left_max <= right_min:
    print(right_min)
else:
    print(-1)
