xa1, ya1, xa2, ya2 = map(int, input().split())
xb1, yb1, xb2, yb2 = map(int, input().split())
xm1, ym1, xm2, ym2 = map(int, input().split())

arr = [[0 for i in range(-1000, 1001)] for j in range(-1000, 1001)]

for x in range(xa1, xa2):
    for y in range(ya1, ya2):
        arr[x][y] = 1

for x in range(xb1, xb2):
    for y in range(yb1, yb2):
        arr[x][y] = 1

for x in range(xm1, xm2):
    for y in range(ym1, ym2):
        arr[x][y] = 0

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 0:
            cnt += 1

print(cnt)