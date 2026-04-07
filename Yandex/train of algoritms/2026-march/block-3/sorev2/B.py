import sys

input = sys.stdin.read
data = input().split()
idx = 0

cases = int(data[idx])
idx += 1
out = []

for _ in range(cases):
    n = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    t = [0] * (n + 1)
    k = [0] * (n + 1)
    pref = [0] * (n + 1)

    for i in range(1, n + 1):
        t[i] = int(data[idx])
        idx += 1
        k[i] = int(data[idx])
        idx += 1
        pref[i] = pref[i - 1] + k[i]

    max_bad = 0
    for j in range(1, n + 1):
        if pref[j - 1] + d > t[j]:
            max_bad = j

    out.append(str(max_bad + 1))

print("\n".join(out))
