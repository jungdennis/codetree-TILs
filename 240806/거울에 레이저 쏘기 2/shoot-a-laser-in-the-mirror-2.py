n = int(input())

arr = []
for i in range(n):
    arr.append(input())

k = int(input())

r, c = 0, 0

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

if k <= n:
    r, c = 0, k-1
    delta = 3
elif k <= 2*n:
    r, c = k-n-1, n-1
    delta = 0
elif k <= 3*n:
    r, c = n-1, n-(k-2*n)
    delta = 1
elif k <= 4*n:
    r, c = n-(k-3*n), 0
    delta = 2

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

cnt = 0
while in_range(r, c):
    mirror = arr[r][c]

    if mirror == '\\':
        if delta == 0:
            delta = 1
        elif delta == 1:
            delta = 0
        elif delta == 2:
            delta = 3
        elif delta == 3:
            delta = 2
    elif mirror == '/':
        delta = 3 - delta

    # print((r, c), (dr[delta], dc[delta]))

    r, c = r+dr[delta], c+dc[delta]
    cnt += 1

print(cnt)