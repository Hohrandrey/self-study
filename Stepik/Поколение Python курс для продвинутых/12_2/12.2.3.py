from random import sample

def get_anagram(word):
    return ''.join(sample(word, len(word)))

print(get_anagram('топорик'))
print(get_anagram('корабль'))
print(get_anagram('барсучка'))
print(get_anagram('математика'))