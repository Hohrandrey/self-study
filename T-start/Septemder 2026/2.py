"""
7
aboba
meow
abobus
abobus
aboba
abobus
aboba
"""
n = int(input())
list_of_words = []
dict_with_counts = {}

for _ in range(n):
    list_of_words.append(input())

for word in set(list_of_words):
    dict_with_counts[word] = list_of_words.count(word)


m_c = max(dict_with_counts.values())
ans = []
for key, val in dict_with_counts.items():
    if val == m_c:
        ans.append(key)
print(' '.join(ans))