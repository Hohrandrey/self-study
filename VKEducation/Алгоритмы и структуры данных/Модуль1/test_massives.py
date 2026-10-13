m =  [1, 2, 3, 4, 5]

l = 0
r = len(m)-1
while l < r:
    m[l], m[r] = m[r], m[l]
    l += 1
    r -= 1

print(m)