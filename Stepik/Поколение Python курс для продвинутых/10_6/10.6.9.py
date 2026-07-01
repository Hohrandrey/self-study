students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}
print({key:val for key, val in students.items() if val[0]>167 and val[1]<75})