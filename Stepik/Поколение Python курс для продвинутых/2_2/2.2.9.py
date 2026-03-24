string = input()

m_r_count = 0
cur_count = 0


if string == 'Р':
    m_r_count = 1
else:
    for elem in string:
        if elem == 'Р':
            cur_count += 1
        else:
            if cur_count > m_r_count:
                m_r_count = cur_count

            cur_count = 0

if cur_count > m_r_count:
    m_r_count = cur_count

print(m_r_count)