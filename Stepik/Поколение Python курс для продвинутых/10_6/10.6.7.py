words = ['yes', 'hello']
print({word:[ord(letter) for letter in word] for word in words})