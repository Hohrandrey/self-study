numbers = [(0, 0, 0, 0), (1, 3), (2, 7, 8)]


def key_min_max_sum(arr):
    return min(arr) + max(arr)


sorted_numers = sorted(numbers, key=key_min_max_sum)
print(sorted_numers)