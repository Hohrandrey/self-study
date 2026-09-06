

file = open('animals2.txt' , 'r', encoding='utf-8')

for line in file:
    print(line.rstrip())

file.close()