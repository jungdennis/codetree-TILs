arr = [[0 for i in range(-100, 101)] for j in range(-100, 101)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 0:
            cnt += 1

print(cnt)