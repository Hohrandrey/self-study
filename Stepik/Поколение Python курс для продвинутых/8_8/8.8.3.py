sentence = 'Dying for the right cause is the most human thing we can do.'
print(*sorted({word.strip(':,.!?();').lower() for word in sentence.split(' ')}))