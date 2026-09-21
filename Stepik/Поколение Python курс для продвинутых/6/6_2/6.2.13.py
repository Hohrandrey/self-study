tuples = [(46, 82), (75,), (3, -4, -10)]

for i in range(len(tuples)):
    tuples[i] = list(tuples[i])
    tuples[i][-1] = 100
    tuples[i] = tuple(tuples[i])

print(tuples)
