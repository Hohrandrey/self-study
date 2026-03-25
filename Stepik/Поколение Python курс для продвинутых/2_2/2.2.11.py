word = input()
text = word + ' запретил букву'

letters = sorted(set(c for c in text if c != ' '))

for letter in letters:
    print(text, letter)
    text = text.replace(letter, '')
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.strip()