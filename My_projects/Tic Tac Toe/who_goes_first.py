import time

def who_goes_first():
    who_goes = input('Кто ходит первым 0 - Вы, 1 - компьютер?\n')
    while who_goes not in ['0', '1']:
        print('Некорректный ввод, попробуйте снова!!!\n')
        time.sleep(1)
        who_goes = input('Кто ходит первым 0 - Вы, 1 - компьютер?\n')
    return who_goes