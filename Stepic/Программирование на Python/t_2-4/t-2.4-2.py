s = input()

result = ''
current = s[0]
count = 1

for i in range(1, len(s)):
    if current == s[i]:
        count += 1
    else:
        result += current + str(count)
        current = s[i]
        count = 1

result += current + str(count)
print(result)