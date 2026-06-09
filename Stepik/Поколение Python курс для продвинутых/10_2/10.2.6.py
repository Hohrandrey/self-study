d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

inp = input()
res =''
for letter in inp:
    letter = letter.upper()
    for elems in d:
        if letter in d[elems]:
            ind = d[elems].index(letter)
            res += elems*(ind+1)
print(res)