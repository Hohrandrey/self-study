def main():
    data = list(map(int, input().split()))
    if not data:
        return
    n = data[0]
    row = data[1:n+1]
    stack = []
    m_a = 0
    for i in range(n + 1):
        c_h = row[i] if i < n else 0
        while stack and row[stack[-1]] > c_h:
            h = row[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            area = h*w
            if area > m_a:
                m_a = area

        stack.append(i)
    print(m_a)


if __name__ == '__main__':
    main()
