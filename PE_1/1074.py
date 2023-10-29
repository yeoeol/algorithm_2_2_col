N, r, c = map(int, input().split())

def ok(x, y, size, n):
    if size == 1:
        return n
    size //= 2
    if x < size and y < size:
        return ok(x, y, size, n)
    elif x < size <= y:
        return ok(x, y-size, size, n+size**2)
    elif x >= size > y:
        return ok(x-size, y, size, n+(size**2)*2)
    else:
        return ok(x-size, y-size, size, n+(size**2)*3)

size = 2**N
print(ok(r, c, size, 0))