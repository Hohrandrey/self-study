st = input()

bad_letters = 'aeiou'

for letter in st:
    if letter in bad_letters:
        st = st.replace(letter, '*')

print(st)
