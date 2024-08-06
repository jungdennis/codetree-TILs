n, m = map(int, input().split())

arr = [[0 for i in range(n)] for j in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

drs = [1, -1, 0, 0]
dcs = [0, 0, 1, -1]

for i in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    arr[r][c] = 1

    cnt = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc

        if in_range(nr, nc) and arr[nr][nc] == 1:
            cnt += 1

    print(1) if cnt == 3 else print(0)