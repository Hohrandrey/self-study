n = int(input())
sp = []
sp_g = []

for i in range(n):
    fam_int = input()
    sp_g.append(fam_int)
    if int(fam_int.split()[-1]) in (4, 5):
        sp.append(fam_int)

print(*sp_g,sep='\n')
print()
print(*sp,sep='\n')
