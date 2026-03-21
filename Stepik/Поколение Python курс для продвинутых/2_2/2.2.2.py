line = list(map(int, input().split()))

c = 0
m_c = 0
for i in range(1, len(line)):
    if line[i-1] < line[i]:
        c+=1
if m_c < c:
        m_c = c
print(m_c)