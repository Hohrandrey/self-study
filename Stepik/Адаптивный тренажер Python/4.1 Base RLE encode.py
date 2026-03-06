inp = input()

letter = []
let_count  = []
count = 1
cur_letter = ''

for i in range(len(inp)):
    if inp[i] != cur_letter:
        if cur_letter:
            letter.append(cur_letter)
            let_count.append(count)
        count = 1
        cur_letter = inp[i]
    else:
        count += 1

letter.append(cur_letter)
let_count.append(count)

for i in range(len(letter)):
    if let_count[i] == 1:
        print(letter[i], end ='')
    else:
        print(str(let_count[i])+letter[i], end='')