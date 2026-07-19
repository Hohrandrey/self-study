from fractions import Fraction

n = int(input())
s = set()
for i in range(1, n):
    for j in range(n, 1, -1):
        if Fraction(i, j) < 1:
            s.add(Fraction(i, j))
print(*sorted(s), sep='\n')