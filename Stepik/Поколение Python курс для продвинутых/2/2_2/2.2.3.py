line = input().split()

for i in range(0, len(line) - 1, 2):
    wrem = line[i]
    line[i] = line[i + 1]
    line[i + 1] = wrem

print(" ".join(line))
