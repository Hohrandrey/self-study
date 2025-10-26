original = input()
result = input()

dic = {}

for i in range(len(original)):
    dic[original[i]] = result[i]

encrypt = input()
decrypt = input()

encrypted = ''
decrypted = ''

for symb in encrypt:
    encrypted += dic[symb]
print(encrypted)

for symb in decrypt:
    for key, value in dic.items():
        if symb == value:
            decrypted += key
print(decrypted)