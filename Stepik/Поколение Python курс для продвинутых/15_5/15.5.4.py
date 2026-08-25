numbers = [14, 15, -1, 2, 0, -42, 36, 2]

def nums_7(x):
    return abs(x) % 7 == 0 and len(str(abs(x)))==2

def square(x):
    return x **2

print(sum(map(square, filter(nums_7, numbers))))