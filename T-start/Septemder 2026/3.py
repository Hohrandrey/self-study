""" Тест 1
3 6
8 1 4 3 5 6
"""

""" Тест 2
3 5
1 2 5 6 7
"""

""" Тест 3
3 6
2 6 7 3 5 9
"""

n, t = map(int, input().split())
a = map(int, input().split())
matrix = [[n*(x-1)+y for y in range(1, n+1)] for x in range(1, n+1)]

def check(matrix):
    for row in matrix:
        if all(cell == 'x' for cell in row):
            return True

        # Проверка столбцов
    for j in range(n):
        if all(matrix[i][j] == 'x' for i in range(n)):
            return True

        # Проверка главной диагонали
    if all(matrix[i][i] == 'x' for i in range(n)):
        return True

        # Проверка побочной диагонали
    if all(matrix[i][n - 1 - i] == 'x' for i in range(n)):
        return True

    return False

for el in a:
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == el:
                matrix[i][j] = 'x'
    print(check(matrix))