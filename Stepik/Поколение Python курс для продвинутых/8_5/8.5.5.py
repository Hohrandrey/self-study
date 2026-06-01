n = int(input())
correct_users = set()
correct_attempts = 0

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

for _ in range(n):
    line = input()
    username, result = line.split(': ')
    if result == 'Correct':
        correct_users.add(username)
        correct_attempts += 1



if correct_users:
    print(f"Верно решили {len(correct_users)} учащихся")
    print(f"Из всех попыток {int_r(correct_attempts / n * 100)}% верных")
else:
    print('Вы можете стать первым, кто решит эту задачу')