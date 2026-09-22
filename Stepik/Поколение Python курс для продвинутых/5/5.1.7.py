matrix = [['.' for _ in range(8)] for _ in range(8)]
dict_letters_to_index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8}

income_data = input()
line = 8 - int(income_data[1])
col = dict_letters_to_index[income_data[0]]


for i in range(8):
    for j in range(8):
        if i == line or j == col or i - j == line-col or i + j == line+col:
            matrix[i][j] = '*'

matrix[line][col] = 'Q'

for row in matrix:
    print(*row)