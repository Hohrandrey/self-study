n = int(input())
iskl_dict = {}
for _ in range(n):
    iskl = input().split()
    classic = iskl[0]
    if len(iskl) > 2:
        iskl_dict[iskl[2]] = {'child' : ''}
        iskl_dict[iskl[2]]['child'] = classic
    else:
        iskl_dict[classic] = None

m = int(input())
anton_iskl_sp = []
for _ in range(m):
    anton_iskl_sp.append(input())

for elem_sp in anton_iskl_sp:
    if elem_sp in iskl_dict.keys() and anton_iskl_sp.index(iskl_dict[elem_sp]['child']) > anton_iskl_sp.index(elem_sp):
        print(iskl_dict[elem_sp]['child'])