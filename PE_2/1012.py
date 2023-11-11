d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    Q = [(x, y)]
    l[x][y] = 0
    while Q:
        ox, oy = Q.pop(0)
        for i in range(4):
            dx = ox+d[i][0]
            dy = oy+d[i][1]
            if 0 > dx or dx >= n or 0 > dy or dy >= m:
                continue
            if l[dx][dy] == 1:
                l[dx][dy] = 0
                Q.append((dx, dy))

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    l = [[0]*m for _ in range(n)]
    cor = []
    result = 0

    for _ in range(k):
        a, b = map(int, input().split())
        l[b][a] = 1
        cor.append((b, a))

    for x, y in cor:
        if l[x][y] == 1:
            bfs(x, y)
            result += 1
    print(result)
