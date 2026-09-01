is_non_negative_num = lambda num: num.replace('.', '').isdigit() and num.count('.')<=1
print(is_non_negative_num('10.45'))