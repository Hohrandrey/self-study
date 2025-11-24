def is_valid_triangle(a: float, b: float, c: float) -> bool:
    if a >= 0 and b >= 0 and c >= 0:
        if a + b > c and a + c > b and b + c > a:
            return True
        return False
    return False

a = int(input())
b = int(input())
c = int(input())

print(is_valid_triangle(a, b, c))