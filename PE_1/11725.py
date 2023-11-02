import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
li = [[]*(n+1) for _ in range(n+1)]

result = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

def dfs(s):
    for item in li[s]:
        if result[item] == 0:
            result[item] = s
            dfs(item)

dfs(1)

for i in range(2, n+1):
    print(result[i])