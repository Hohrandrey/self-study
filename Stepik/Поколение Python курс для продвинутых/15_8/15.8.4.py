is_num = lambda num: num[1:].replace('.', '').isdigit() and num.count('.')<=1 if num[0] == '-' else num.replace('.', '').isdigit() and num.count('.')<=1
print(is_num('-18'))