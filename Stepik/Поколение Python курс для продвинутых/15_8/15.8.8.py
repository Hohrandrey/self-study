data = [
   'работа', 'слово', 'место', 'лицо', 'друг',
   'глаз', 'вопрос', 'дом', 'сторона',
]

alf_sorted = sorted(data)
len_sorted = sorted(alf_sorted, key = lambda item: len(item))
print(*len_sorted)