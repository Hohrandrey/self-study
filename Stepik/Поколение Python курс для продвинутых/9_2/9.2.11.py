m = int(input())
st_fams = set(input() for _ in range(int(input())))

for _ in range(m-1):
    st_fams &= set(input() for _ in range(int(input())))

print(*sorted(st_fams), sep='\n')