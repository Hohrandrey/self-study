inp_colors = map(int, input().split())

print(*map(lambda color: 255-color, inp_colors))