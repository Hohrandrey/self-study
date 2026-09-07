import random

def get_random_string(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    return random.choice(file.readlines()).rstrip()

print(get_random_string('animals2.txt'))
print(get_random_string('animals1.txt'))
print(get_random_string('animals3.txt'))