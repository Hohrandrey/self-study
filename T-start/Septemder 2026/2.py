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


list_of_words = []
dict_with_counts = {}

for _ in range(int(input())):
    word = input()
    dict_with_counts[word] = dict_with_counts.get(word, 0) + 1


m_c = max(dict_with_counts.values())
ans = []
for key, val in dict_with_counts.items():
    if val == m_c:
        ans.append(key)


print(" ".join(sorted(ans)))
