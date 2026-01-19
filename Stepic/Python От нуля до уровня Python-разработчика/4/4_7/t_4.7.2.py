class TooShortPasswordError(Exception):
    pass


def check_password(p):
    if len(p) < 8:
        raise TooShortPasswordError


password = input()
try:
    check_password(password)
except TooShortPasswordError:
    print("Пароль слишком короткий!")
else:
    print("Пароль нормальный")
