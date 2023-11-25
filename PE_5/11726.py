def solve():
    l = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1): # 0층 초기화
        l[0][i] = i

    for floor in range(1, k+1):
        for ho in range(1, n+1):
            summ = 0
            for i in range(1, ho+1):
                summ += l[floor-1][i]
            l[floor][ho] = summ
    print(l[k][n])

T = int(input())
for _ in range(T):
    k = int(input()) #층
    n = int(input()) #호
    solve()