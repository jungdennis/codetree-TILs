import sys

n, r, c = map(int, sys.stdin.readline().rstrip().split())
r -= 1
c -= 1

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = []

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]
while True:
    visited.append(arr[r][c])

    flag = False
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if is_range(nr, nc) and arr[nr][nc] > arr[r][c]:
            r_, c_ = nr, nc
            flag = True

    if flag:
        r, c = r_, c_
    else:
        break

for num in visited:
    print(num, end = ' ')