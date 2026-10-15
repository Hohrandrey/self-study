int(input())
arr=input().split()
del_num = input()
print(*filter(lambda el: el != del_num,arr))