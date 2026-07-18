text = 'XoʮeɯƄ зapaбaтыʙaтƄ oт 5K ʙ cyтkͷ? Haπͷɯͷ ʜaʍ ʙ ʮaтe.'
homoglyphs = {
    'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а',
    'ʍ': 'м', 'ʙ': 'в', 'Φ': 'Ф', 'k': 'к', 'x': 'х',
    'c': 'с', 'E': 'Е', 'T': 'Т', 'ȹ': 'ф', 'Ͷ': 'И',
    'ʜ': 'н', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н',
    'K': 'К', 'Ƅ': 'ь', 'ͷ': 'и', 'ɯ': 'ш', 'X': 'Х',
    'C': 'С', 'B': 'В', 'M': 'М', 'π': 'п', '3': 'З',
    'Γ': 'Г', 'ʮ': 'ч',
}

def replace_homoglyphs(text):
    string = ''
    for elem in text:
        string += homoglyphs.get(elem, elem)
    return string

print(replace_homoglyphs(text))