import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
k -= 1

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

r = 0
while True:
    if r >= n:
        break

    flag = 1
    for c in range(k, k + m):
        if arr[r][c] == 0:
            flag *= 1
        else:
            flag *= 0

    if flag:
        r += 1
    else:
        break

r -= 1
for c in range(k, k + m):
    arr[r][c] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()