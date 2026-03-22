line = input().split()

new_line = [line[-1]] + line[:-1]
print(*new_line)
