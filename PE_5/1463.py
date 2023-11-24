import sys
n = int(input())
num = 1
c = sys.maxsize
def solve1(a, cnt):
    global c
    if a == n:
        c = min(c, cnt)
        return
    if a > n:
        return
    solve1(a*3, cnt+1)
    solve1(a*2, cnt+1)
    solve1(a+1, cnt+1)

def solve2(a):
    l = [sys.maxsize for _ in range(a+1)]
    l[0] = 0
    l[1] = 0
    for i in range(1, a+1):
        if i*3 <= a:
            l[i*3] = min(l[i]+1, l[i*3])
        if i*2 <= a:
            l[i*2] = min(l[i]+1, l[i*2])
        if (i+1) <= a:
            l[i+1] = min(l[i]+1, l[i+1])
    return l[a]

print(solve2(n))