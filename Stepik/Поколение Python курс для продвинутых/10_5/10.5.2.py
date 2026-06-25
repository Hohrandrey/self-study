def transform(text):
    dic = {}
    for i in range(len(text)):
        dic.setdefault(text[i], set()).add(i)
    return dic

print(transform('Аметист'))