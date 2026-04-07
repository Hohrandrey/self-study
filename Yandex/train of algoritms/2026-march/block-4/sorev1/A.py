n, m = map(int, input().split())

if n < 0 or m < 0:
    print(-2)
    exit()

grid = [list(input().strip()) for _ in range(n)]

retrovirus = 0

visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cx >= n or cy < 0 or cy >= m or visited[cx][cy] or grid[cx][cy] != '#':
            continue
        visited[cx][cy] = True
        stack.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#' and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)