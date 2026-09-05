"""
6 9
2 2 8 0 -6 -9
"""
"""
7 20
3 2 2 -6 -7 0 0
"""
"""
6 4
2 2 8 0 -6 -9
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
S = []
for i in range(n-1):
    for j in range(i+1, n):
        S.append(a[i]*a[j])
S.sort()
print(S[k-1])