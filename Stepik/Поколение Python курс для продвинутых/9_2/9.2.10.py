su = list(input() for _ in range(int(input())+int(input())))
su_set = set(su)
print(len(su_set)-(len(su)-len(su_set)) or 'NO')