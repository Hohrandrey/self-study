n = int(input())
row = list(map(int, input().split()))
target = int(input())

l = 0
r = n - 1
ans = None

while l <= r:
    middle = (l + r) // 2
    if row[middle] < target:
        l = middle + 1
    elif row[middle] > target:
        r = middle - 1
    else:
        ans = middle
        break

if ans is None:
    print(r+1)
else:
    print(ans)