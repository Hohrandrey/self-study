int(input())
stack = list(filter(lambda x: int(x) % 2 == 0, input().split()))
if stack:
    print(stack[-1])
else:
    print(-1)