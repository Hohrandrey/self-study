class OutOfRangeError(Exception):
    pass


def check_range(x, min_val, max_val):
    if x < min_val or x > max_val:
        raise OutOfRangeError


x = int(input())
min_val = int(input())
max_val = int(input())
try:
    check_range(x, min_val, max_val)
except OutOfRangeError:
    print("Число вне диапазона!")
else:
    print("Число в диапазоне")
