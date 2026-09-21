points = [(3, 4), (-2, 1), (0, 1), (5, 12)]


def lenght(arr):
    x, y = arr[0], arr[1]
    return (x**2 + y**2) ** 0.5


print(sorted(points, key=lenght))
