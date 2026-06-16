n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
row, col = 0, 0
dir_index = 0

for num in range(1, n*m+1):
    matrix[row][col] = num

    n_row = row + direction[dir_index][0]
    n_col = col + direction[dir_index][1]

    if (n_row < 0 or n_row >= n or
            n_col < 0 or n_col >= m or
            matrix[n_row][n_col] != 0):
        dir_index = (dir_index + 1) % 4
        n_row = row + direction[dir_index][0]
        n_col = col + direction[dir_index][1]

    col = n_col
    row = n_row

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()