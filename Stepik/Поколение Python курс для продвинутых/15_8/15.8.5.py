words = ['justice', 'orange', 'plant', 'sunday']

filtered_and_sorted_words = sorted(filter(lambda word: len(word) == 6, words))
print(*filtered_and_sorted_words)