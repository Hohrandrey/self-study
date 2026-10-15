    int(input())
    arr = tuple(sorted(map(int,input().split())))

    m_d = float("inf")
    pair = -1, -1

    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        if m_d > diff:
            m_d = diff
            pair = (arr[i],arr[i+1])

    print(pair[0],pair[1])