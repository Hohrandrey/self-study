from random import choice, randint
import time


def show_field(matrix):
    for line in matrix:
        print(*line)
    print()


def ask_for_game(first_game):
    if first_game:
        list_first = ['Здравствуйте! Не желаете ли сыграть?', 'Доброго времени суток! Хотите поиграть?', 'Привет! Как насчет игры?']
        print(choice(list_first))
    else:
        list_not_first = ['Сыграем еще разок?', 'Хотите еще сыграть?', 'Желаете еще раз?']
        print(choice(list_not_first))


def who_goes_first():
    who_goes = input('Кто ходит первым 0 - Вы, 1 - компьютер?\n')
    while who_goes not in ['0', '1']:
        print('Некорректный ввод, попробуйте снова!!!\n')
        time.sleep(1)
        who_goes = input('Кто ходит первым 0 - Вы, 1 - компьютер?\n')
    return who_goes


def get_user_move(matrix, symbol):
    row, column = int(input('Введите строку\n')), int(input('Введите столбец\n'))
    while matrix[row-1][column-1] != '⬜':
        print('Выбранная ячейка не пустая!!!\n')
        row, column = int(input('Введите строку\n')), int(input('Введите столбец\n'))
    matrix[row-1][column-1] = symbol
    print(f'Ваш ход {row} ряд {column} столбец\n')


def get_computer_move(matrix, symbol):
    row = randint(0, 2)
    column = randint(0, 2)
    while matrix[row][column] != '⬜':
        row = randint(0, 2)
        column = randint(0, 2)
    matrix[row][column] = symbol
    print(f'Ход компьютера {row+1} ряд {column+1} столбец\n')


def check_result(matrix):
    win_lines = [
        [matrix[0][0], matrix[0][1], matrix[0][2]],
        [matrix[1][0], matrix[1][1], matrix[1][2]],
        [matrix[2][0], matrix[2][1], matrix[2][2]],
        [matrix[0][0], matrix[1][0], matrix[2][0]],
        [matrix[0][1], matrix[1][1], matrix[2][1]],
        [matrix[0][2], matrix[1][2], matrix[2][2]],
        [matrix[0][0], matrix[1][1], matrix[2][2]],
        [matrix[0][2], matrix[1][1], matrix[2][0]],
    ]
    return ['❌','❌','❌'] in win_lines or ['⭕','⭕','⭕'] in win_lines


def main_game():
    matrix = [['⬜' for _ in range(3)] for _ in range(3)]
    f_game = True
    ask_for_game(f_game)
    continue_game = input('да - продолжить, нет - выйти\n').lower()

    while continue_game not in ('да', 'нет'):
        print('Некорректный ввод, попробуйте снова!!!\n')
        continue_game = input('да - продолжить, нет - выйти\n').lower()

    if continue_game == 'да':
        f_game = False
        symbol_num = 1
        start_person = int(who_goes_first())
        cur_person = start_person
        while ('⬜' in matrix[0] or '⬜' in matrix[1] or '⬜' in matrix[2]) and not check_result(matrix):
            symbol = '❌' if symbol_num % 2 == 1 else '⭕'
            if cur_person % 2 == 0:
                get_user_move(matrix, symbol)
            else:
                get_computer_move(matrix, symbol)

            show_field(matrix)
            cur_person += 1
            symbol_num += 1

        if not check_result(matrix):
            print('Ничья!')
        else:
            print('Компьютер 🤖 победил =(' if start_person == 1 else 'Ты победил(а)! Поздравляем! 🎉🎉')
    else:
        return


main_game()