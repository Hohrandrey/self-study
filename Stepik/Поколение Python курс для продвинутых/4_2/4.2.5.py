list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

s = 0
c = 0
for elem in list1:
    c += len(elem)
    s += sum(elem)
print(s/c)