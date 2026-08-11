

def greet(name, *args):
    hel = 'Hello, ' + name
    if args:
        hel += ' and '
        hel += ' and '.join(args)
    return hel + '!'

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))