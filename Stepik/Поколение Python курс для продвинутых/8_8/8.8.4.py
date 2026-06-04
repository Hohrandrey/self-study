sentence = 'Dying for the right cause is the most human thing we can do.'
s = set()
for word in sentence.split(' '):
    if len(word.strip(':,.!?();').lower()) < 4:
        s.add(word.strip(':,.!?();').lower())
print(*sorted(s))
#print(*sorted({word.strip(':,.!?();').lower() for word in sentence.split(' ') if len(word.strip(':,.!?();').lower()) < 4}))