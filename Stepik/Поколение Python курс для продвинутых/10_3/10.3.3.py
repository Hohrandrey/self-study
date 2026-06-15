text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
result = {}
for letter in set(text):
    result[letter] = text.count(letter)
print(result)