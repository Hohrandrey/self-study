numbers = [14 + 7j, 13 - 5j, 8 + 2j, 1 + 3j, 55 - 4j, 2 - 3j]
print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))