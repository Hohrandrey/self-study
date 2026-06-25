from random import randint

def generate_password(n):
    string = ''
    for _ in range(n):
        if randint(0, 1) == 0:
            string += chr(randint(65, 90))
        else:
            string += chr(randint(97, 122))
    return string
