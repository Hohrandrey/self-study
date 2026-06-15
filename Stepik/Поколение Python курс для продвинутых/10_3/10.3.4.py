text = 'bridge snake island game glory eye arrogant car nature game glory game'
result = {}
for letter in set(text.split()):
    result[letter] = text.count(letter)


m_val = max(result.values())
m_key = []
for key in result:
    if m_val == result[key]:
        m_key.append(key)
print(min(m_key))