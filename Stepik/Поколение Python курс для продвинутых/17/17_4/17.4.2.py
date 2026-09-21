from random import randint

def write_random_numbers(n):
    with open('random.txt', 'w', encoding='utf-8') as f:
        for _ in range(n):
            f.write(str(randint(111, 777))+'\n')

write_random_numbers(4)
with open('random.txt') as f:
    print(f.read())
