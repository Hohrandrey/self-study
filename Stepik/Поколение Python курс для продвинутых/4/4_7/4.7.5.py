A = [[1, 0], [4, 1]]


def multiply_matrices(X, Y):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += X[i][k] * Y[k][j]
    return result


result = [[1, 0], [4, 1]]

for _ in range(24):
    result = multiply_matrices(result, A)

print(result)
