res = {}

with open('dataset_3363_3.txt', 'r') as file:
    line = file.read().lower().split()


for l in range(len(line)):
    if line[l] not in res:
        res[line[l]] = line.count(line[l])

m_v = 0
res_key = 'zzzzzzzz'
for key, val in res.items():
    if val > m_v:
        m_v = val
        res_key = key
    elif val == m_v and key < res_key:
        res_key = key

print(res_key, m_v)