from fractions import Fraction
n =int(input())

res =[]

for i in range(1, n+1):
    for j in range(1, n+1):
        fr = Fraction(i, j)
        if fr.numerator < fr.denominator and fr.numerator + fr.denominator == n:
            res.append(fr)
print(max(res))