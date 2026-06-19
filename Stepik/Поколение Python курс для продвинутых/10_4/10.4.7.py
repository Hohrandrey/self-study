"""
*!*!*?
3
а: 3
н: 2
с: 1
"""

enc_word = input()
word_c = {elem : enc_word.count(elem) for elem in enc_word}
annot = {}
for _ in range(int(input())):
    letter, count = input().split(': ')
    annot[letter] = int(count)

string  = ''
for elem in enc_word:
    found_c = word_c[elem]
    for letter, count in annot.items():
        if found_c  == count:
            string += letter

print(string)