n = int(input())
arr = [[0 for i in range(-100, 101)] for j in range(-100, 101)]

for i in range(n):
    if i % 2 == 0:
        color = 1       # red
    else:
        color = 2       # blue

    x1, y1, x2, y2 = map(int, input().split())

    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = color

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            cnt += 1
print(cnt)