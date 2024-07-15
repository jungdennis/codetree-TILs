import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
happy = 0
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

for r in range(n):
    max_cnt = 0
    cnt = 1
    temp = grid[r][0]
    for j in range(1, n):
        if grid[r][j] == temp:
            cnt += 1
        else:
            cnt = 1

        if cnt >= max_cnt:
            max_cnt = cnt

        temp = grid[r][j]

    if max_cnt >= m:
        happy += 1

for c in range(n):
    max_cnt = 0
    cnt = 1
    temp = grid[0][c]
    for i in range(1, n):
        if grid[i][c] == temp:
            cnt += 1
        else:
            cnt = 1

        if cnt >= max_cnt:
            max_cnt = cnt
        temp = grid[i][c]

    if cnt >= m:
        happy += 1

print(happy)