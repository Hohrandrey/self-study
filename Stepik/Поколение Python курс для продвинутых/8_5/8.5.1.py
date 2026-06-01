n = int(input())
sp = []
lens = []
for i in range(n):
    sp.append(input().lower())
    lens.append(len(set(sp[i])))

print(*lens, sep='\n')