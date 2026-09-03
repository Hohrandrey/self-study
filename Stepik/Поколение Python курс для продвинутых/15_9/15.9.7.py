n = int(input())
res = []
for _ in range(n):
    k = int(input())
    cur_klass = []
    for _ in range(k):
        student = input()
        cur_klass.append("5" in student)
    res.append(any(cur_klass))

print("YES" if all(res) else "NO")
