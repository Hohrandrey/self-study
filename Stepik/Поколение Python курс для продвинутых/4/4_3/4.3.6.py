string = input().split()
n = int(input())


def chunked(string, n):
    chanks = []
    for i in range(0, len(string), n):
        chanks.append(string[i : i + n])
    return chanks


print(chunked(string, n))
