numbers = [854, 10, 5, 452, 478, 236, 202, 41]


def thre_52(num):
    return num % 5 == 2 and len(str(num)) == 3

def square(num):
    return num * num * num

new_filtered = list(filter(thre_52, numbers))
new_mapped = map(square, new_filtered)
print(*new_mapped, sep='\n')