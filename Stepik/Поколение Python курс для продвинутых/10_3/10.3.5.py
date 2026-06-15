pets = [
    ('Freddie', 'Jessica', 'Brown', 38),
    ('Freya', 'Jessica', 'Brown', 38),
    ('Chernysh', 'Harry', 'Wonn', 20),
    ('Kesha', 'Harry', 'Wonn', 20),
    ('Patrick', 'Hermann', 'Schulz', 72),
    ('Foxya', 'Julia', 'Alikina', 47),
    ('Thomas', 'Julia', 'Alikina', 47),
    ('Mia', 'Nikolai', 'Lagunov', 39),
    ('Rufus', 'Harry', 'Wonn', 20),
]
res = {}
for pet in pets:
    res[pet[1:4]] = res.get(pet[1:4], []) + [pet[0]]
print(res)