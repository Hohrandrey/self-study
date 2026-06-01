nums = input().split()
s = set()

for el in nums:
    el = int(el)
    if el not in s:
        s.add(el)
        print("NO")
    else:
        print("YES")