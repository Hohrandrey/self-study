def modify_list(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0:
            new_lst.append(num // 2)
    lst.clear()
    lst.extend(new_lst)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)