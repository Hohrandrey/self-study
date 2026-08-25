numbers = [(0, 0), (1, 1), (2, 2, 2), (3,)]


def comp_sred(arr):
    return sum(arr)/len(arr)

print(min(numbers, key=comp_sred))
print(max(numbers, key=comp_sred))