data = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]

sorted_data = sorted(data, key=lambda pair: pair[1][-1], reverse=True)
for count, city in sorted_data:
    print(f"{city}: {count}")
