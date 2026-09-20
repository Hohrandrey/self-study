import os
from who_goes_first import who_goes_first
from check_result import check_result
from ask_for_game import ask_for_game
from get_computer_move import get_computer_move
from get_user_move import get_user_move


def show_field(matrix):
    for line in matrix:
        print(*line)
    print()


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main_game():
    matrix = [['⬜' for _ in range(3)] for _ in range(3)]
    f_game = True
    ask_for_game(f_game)
    f_game = False
    continue_game = input('да - продолжить, нет - выйти\n').lower()

    while continue_game not in ('да', 'нет'):
        print('Некорректный ввод, попробуйте снова!!!\n')
        continue_game = input('да - продолжить, нет - выйти\n').lower()

    while True:
        if continue_game == 'да':
            clear_console()
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
                print('Компьютер 🤖 победил =(' if cur_person % 2 == 0 else 'Ты победил(а)! Поздравляем! 🎉🎉')
            ask_for_game(f_game)
            continue_game = input('да - продолжить, нет - выйти\n').lower()

            while continue_game not in ('да', 'нет'):
                print('Некорректный ввод, попробуйте снова!!!\n')
                continue_game = input('да - продолжить, нет - выйти\n').lower()

            matrix = [['⬜' for _ in range(3)] for _ in range(3)]
        else:
            return


main_game()