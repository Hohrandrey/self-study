""" Тест 1
3 6
8 1 4 3 5 6
"""

""" Тест 2
3 5
1 2 5 6 7
"""

""" Тест 3
3 6
2 6 7 3 5 9
"""

n, t = map(int, input().split())
a = map(int, input().split())
matrix = [[n*(x-1)+y for y in range(1, n+1)] for x in range(1, n+1)]
print(matrix)
