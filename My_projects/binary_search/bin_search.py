

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess < x:
            low = mid + 1
        elif guess > x:
            high = mid - 1
        else:
            return arr[mid]
    return None


print(binary_search([1,2,3,4,5], 1))