m = int(input())
n = int(input())
home_bible = list(input() for _ in range(m))
sum_list = list(input() for _ in range(n))

for elem in sum_list:
    if elem in home_bible:
        print('YES')
    else:
        print('NO')
