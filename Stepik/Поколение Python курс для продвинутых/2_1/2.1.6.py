num = input()

if len(num)==5:
    num = num[::-1]
else:
    num = num[0] + num[:-6:-1]
print(int(num))