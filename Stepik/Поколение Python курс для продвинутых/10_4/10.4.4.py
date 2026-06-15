dictionary_synonyms = {}
for _ in range(int(input())):
    key, value = input().split()
    dictionary_synonyms[key] = value

que = input()
for key, value in dictionary_synonyms.items():
    if que == value:
        print(key)
    elif que == key:
        print(value)
