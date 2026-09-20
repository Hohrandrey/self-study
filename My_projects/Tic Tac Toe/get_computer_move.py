from random import randint

def get_computer_move(matrix, symbol):
    row = randint(0, 2)
    column = randint(0, 2)
    while matrix[row][column] != '⬜':
        row = randint(0, 2)
        column = randint(0, 2)
    matrix[row][column] = symbol
    print(f'Ход компьютера {row+1} ряд {column+1} столбец\n')