n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    cnt += k // l[-1-i]
    k %= l[-1-i]

print(cnt)