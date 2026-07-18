def scrabble(letters, word):
    word, letters = word.lower(), letters.lower()
    for elem in set(word):
        if word.count(elem) > letters.count(elem):
            return False
    return True


print(scrabble('', 'abcde'))