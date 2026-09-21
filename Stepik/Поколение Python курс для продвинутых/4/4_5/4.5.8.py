plate = input()

letter_to_id = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
matrix = [["." for _ in range(8)] for _ in range(8)]
line = 8 - int(plate[1])
table = letter_to_id[plate[0]]

matrix[line][table] = "N"


if line + 2 < 8 and table + 1 < 8:
    matrix[line + 2][table + 1] = "*"

if line + 2 < 8 and table - 1 >= 0:
    matrix[line + 2][table - 1] = "*"

if line - 2 >= 0 and table - 1 >= 0:
    matrix[line - 2][table - 1] = "*"

if line - 2 >= 0 and table + 1 < 8:
    matrix[line - 2][table + 1] = "*"

if line - 1 >= 0 and table + 2 < 8:
    matrix[line - 1][table + 2] = "*"

if line - 1 >= 0 and table - 2 >= 0:
    matrix[line - 1][table - 2] = "*"

if line + 1 < 8 and table + 2 < 8:
    matrix[line + 1][table + 2] = "*"

if line + 1 < 8 and table - 2 >= 0:
    matrix[line + 1][table - 2] = "*"


for line in matrix:
    print(*line)
