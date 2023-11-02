n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(s):
    visited[s] = True
    print(s, end=" ")
    for item in graph[s]:
        if not visited[item]:
            dfs(item)
def bfs(s):
    Q = [s]
    visited2[s] = True
    while Q:
        q = Q.pop(0)
        print(q, end=" ")
        for item in graph[q]:
            if not visited2[item]:
                visited2[item] = True
                Q.append(item)

visited = [False]*(n+1)
visited2 = [False]*(n+1)

dfs(v)
print()
bfs(v)