from random import choice


def ask_for_game(first_game):
    if first_game:
        list_first = ['Здравствуйте! Не желаете ли сыграть?', 'Доброго времени суток! Хотите поиграть?', 'Привет! Как насчет игры?']
        print(choice(list_first))
    else:
        list_not_first = ['Сыграем еще разок?', 'Хотите еще сыграть?', 'Желаете еще раз?']
        print(choice(list_not_first))