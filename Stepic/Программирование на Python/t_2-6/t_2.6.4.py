start_matr = []
res_matr = []

while True:
    line = input().strip()
    if line == "end":
        break
    row = list(map(int, line.split()))
    start_matr.append(row)

rows = len(start_matr)
colums = len(start_matr[0])
