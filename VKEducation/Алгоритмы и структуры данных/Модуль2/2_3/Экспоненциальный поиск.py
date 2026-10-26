n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def exponential_search(arr, n, target):
    border = 1
    while border < n and arr[border] < target:
        border *= 2

    if border > n:
        return border // 2, n
    else:
        return border // 2, border

print(*exponential_search(arr, n, target))