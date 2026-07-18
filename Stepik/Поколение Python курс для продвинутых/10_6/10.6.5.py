s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'

print({int(item.split(':')[0]) : item.split(':')[1] for item in s.split()})