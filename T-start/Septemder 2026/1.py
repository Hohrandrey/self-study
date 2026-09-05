"""
4
1 2 1 2
"""
"""
4
6 7 6 9
"""
"""
3
1 2 1
"""


n = int(input())
a = list(map(int, input().split()))

total = sum(a)
if total % (n - 1) != 0:
    print("NO")
else:
    S = total // (n - 1)
    count_S = sum(1 for x in a if x == S)

    if count_S >= n - 2:
        remaining = [x for x in a if x != S]

        if len(remaining) == 0:
            print("YES")
        elif len(remaining) == 1:
            print("YES" if remaining[0] == S else "NO")
        elif len(remaining) == 2:
            print("YES" if sum(remaining) == S else "NO")
        else:
            print("NO")
    else:
        print("NO")