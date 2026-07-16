WRX = {'execute':"X", 'read' : 'R', 'write' : 'W'}
files_inf = {}
for i in range(int(input())):
    file, op = input().split(' ', 1)
    files_inf[file] = files_inf.get(file, '') + op

ans = []
for x in range(int(input())):
    com, file = input().split(' ')

    if WRX[com] in files_inf[file]:
        ans.append('OK')
    else:
        ans.append('Access denied')
print(*ans, sep='\n')