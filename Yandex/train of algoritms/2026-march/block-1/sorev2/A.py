n = int(input())

string = input()

max_count = 0

count = 1

if len(string) == 1 and (string == "a" or string == "h"):
    max_count = 1
else:
    for i in range(n - 1):
        if (string[i] == "h" and string[i + 1] == "a") or (
            string[i] == "a" and string[i + 1] == "h"
        ):
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count

print(max_count)
