n = int(input())

trib = [1,1,1]

for i in range(n-3):
    trib_ch = sum(trib[i:i+3])
    trib.append(trib_ch)

print(*trib[:n])