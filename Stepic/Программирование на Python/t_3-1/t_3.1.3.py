def modify_list(lst):
    i = 0
    while i <= len(lst):
        i+=1
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
        else:
            lst.remove(lst[i])


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)