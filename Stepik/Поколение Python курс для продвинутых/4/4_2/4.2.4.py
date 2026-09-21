list1 = [[1, 7], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103, 413], [1, 2, 3]]

m = -1
for elem in list1:
    if max(elem) > m:
        m = max(elem)
print(m)
