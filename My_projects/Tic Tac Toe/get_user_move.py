def get_user_move(matrix, symbol):
    row, column = int(input('Введите строку\n')), int(input('Введите столбец\n'))
    while matrix[row-1][column-1] != '⬜':
        print('Выбранная ячейка не пустая!!!\n')
        row, column = int(input('Введите строку\n')), int(input('Введите столбец\n'))
    while row not in (0, 1, 2) or column not in (0, 1, 2):
        row, column = int(input('Введите строку\n')), int(input('Введите столбец\n'))
    matrix[row-1][column-1] = symbol
    print(f'Ваш ход {row} ряд {column} столбец\n')