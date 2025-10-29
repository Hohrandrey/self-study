sp = input().split()
result = round(sp.count('A') / len(sp), 2)
print(f"{result:.2f}")