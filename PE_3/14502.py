import copy
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
lab = [list(map(int, stdin.readline().split())) for _ in range(n)]

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(count+1)
                lab[i][j] = 0


result = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    Q = deque()
    test = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if test[i][j] == 2:
                Q.append((i, j))
    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            dx = cx+d[i][0]
            dy = cy+d[i][1]
            if (0 <= dx < n) and (0 <= dy < m):
                if test[dx][dy] == 0:
                    test[dx][dy] = 2
                    Q.append((dx, dy))

    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                cnt += 1

    result = max(result, cnt)


make_wall(0)
print(result)