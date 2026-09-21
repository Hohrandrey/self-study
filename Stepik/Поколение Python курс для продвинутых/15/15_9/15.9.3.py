abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))


res = []
for x, y, z in zip(abscissas, ordinates, applicates):
    res.append(x**2 + y**2 + z**2 <= 4)

print(all(res))
