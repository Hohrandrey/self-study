file = open(input(), 'r', encoding='utf-8')

print(file.readlines()[-2].rstrip())

file.close()