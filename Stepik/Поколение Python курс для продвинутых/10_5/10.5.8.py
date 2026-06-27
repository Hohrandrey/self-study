clients_dic = {}

def bank(operation, id, amount):
    if operation == 'show balance':
        print(clients_dic.get(id, 0))
    elif operation == 'top up':
        clients_dic[id] = clients_dic.get(id, 0) + amount
    elif operation in {'withdraw', 'pay'}:
        clients_dic[id] = clients_dic.get(id, 0) - amount
