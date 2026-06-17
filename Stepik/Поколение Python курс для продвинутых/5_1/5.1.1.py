lis = input().split()
n = int(input())
print([lis[i::n] for i in range(n)])