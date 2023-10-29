N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

result = [0, 0, 0]

def ok(x, y, size):
    first = matrix[x][y]
    for i in range(x, size + x):
        for j in range(y, size + y):
            if matrix[i][j] != first:
                for k in range(3):
                    for z in range(3):
                        ok(x+k*size//3, y+z*size//3, size//3)
                return
    result[first] += 1

ok(0, 0, N)
print(result[-1])
print(result[0])
print(result[1])