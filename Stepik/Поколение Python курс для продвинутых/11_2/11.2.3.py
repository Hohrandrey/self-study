letter_price = {'AEILNORSTU':1, 'DG':2, 'BCMP':3, 'FHVWY':4, 'K':5, 'JX':8, 'QZ':10}

inp = input()
s = 0
for key, value in letter_price.items():
    for letter in inp:
        if letter in key:
            s+=value
print(s)