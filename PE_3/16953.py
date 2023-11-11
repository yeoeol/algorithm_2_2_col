from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))

def solve():
    while q:
        pa, pt = q.popleft()
        if pa > b:
            continue
        if pa == b:
            print(pt)
            break
        q.append((int(str(pa)+'1'), pt+1))
        q.append((pa*2, pt+1))

solve()
if len(q)==0:
    print(-1)