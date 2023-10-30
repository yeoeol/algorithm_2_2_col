l, w, h = map(int, input().split())
total = l * w * h
n = int(input())
a = []
for _ in range(n):
    A, B = map(int, input().split())
    A = 2**A
    a.append([A, B])
a.sort(reverse=True)

answer, total_now = 0, 0
for leng, cnt in a:
    total_now *= 8
    cur = (l // leng) * (w // leng) * (h // leng) - total_now
    cur = min(cur, cnt)

    answer += cur
    total_now += cur
if total_now == total:
    print(answer)
else:
    print(-1)
