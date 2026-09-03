password = tuple(input())
l = any(map(lambda el: el.islower(), password))
u = any(map(lambda el: el.isupper(), password))
d = any(map(lambda el: el.isdigit(), password))
lenght = len(password) >= 7
print('YES' if all([l,u,d,lenght]) else 'NO')