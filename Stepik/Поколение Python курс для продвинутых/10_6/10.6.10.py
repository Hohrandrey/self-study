tuples = [(26, 1, 30), (47, 5, 4), (11, 7, 9)]
print({elem[0] : elem[1:] for elem in tuples})