int(input())
arr=list(map(int,input().split()))
arr_no_zer=list(filter(lambda el: el != 0,arr))
print(*arr_no_zer+[0]*(len(arr)-len(arr_no_zer)))