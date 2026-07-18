import string
from random import choice

n = int(input())
m = int(input())
letters_up = ''.join(set(string.ascii_uppercase) - set('lIoO'))
letters_down = ''.join(set(string.ascii_lowercase) - set('lIo'))
nums = ''.join(set(string.digits) - set('10'))


def generate_password(length):
    passw = choice(letters_up) + choice(letters_down) + choice(nums)
    for i in range(length-3):
        passw += choice(letters_up+letters_down+nums)
    return passw


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

generate_passwords(n, m)