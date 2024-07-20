arr = [[0 for i in range(-1000, 1001)] for j in range(-1000, 1001)]

xa1, ya1, xa2, ya2 = map(int, input().split())
xa1 += 1000
ya1 += 1000
xa2 += 1000
ya2 += 1000

xb1, yb1, xb2, yb2 = map(int, input().split())
xb1 += 1000
yb1 += 1000
xb2 += 1000
yb2 += 1000


for x in range(xa1, xa2):
    for y in range(ya1, ya2):
        arr[x][y] = 1

for x in range(xb1, xb2):
    for y in range(yb1, yb2):
        arr[x][y] = 0

x = []
y = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 0:
            x.append(i)
            y.append(j)

if len(x) != 0:
    x_min, x_max = min(x), max(x)
else:
    x_min, x_max = 0, 0

if len(y) != 0:
    y_min, y_max = min(y), max(y)
else:
    y_min, y_max = 0, 0
    
print((x_max - x_min + 1) * (y_max - y_min + 1))