tim = input()
rus = input()

if tim == rus:
    print("ничья")
elif (
    tim == "камень"
    and rus == "ножницы"
    or tim == "ножницы"
    and rus == "бумага"
    or tim == "бумага"
    and rus == "камень"
):
    print("Тимур")
else:
    print("Руслан")
