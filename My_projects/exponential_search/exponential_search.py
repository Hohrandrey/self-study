n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def binary_search(arr, l,r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    return None

def exponential_search(arr, n, target):
    border = 1
    while border < n and arr[border] < target:
        border *= 2

    if border > n:
        return binary_search(arr, border // 2, n, target)
    else:
        return binary_search(arr, border // 2, border, target)

print(exponential_search(arr, n, target))