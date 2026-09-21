timur_move = input()
ruslan_move = input()

moves = ["Спок", "ножницы", "бумага", "камень", "ящерица"]
outcomes = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

dif = moves.index(timur_move) - moves.index(ruslan_move)
res = outcomes[dif]
print(res)
