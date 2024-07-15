import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
happy = 0
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

for r in range(n):
    max_cnt = 1
    cnt = 1
    temp = 0
    for j in range(n):
        if grid[r][j] == temp:
            cnt += 1
        else:
            temp = grid[r][j]
            cnt = 1

        if cnt >= max_cnt:
            max_cnt = cnt
        
    if max_cnt >= m:
        happy += 1

for c in range(n):
    max_cnt = 1
    cnt = 1
    temp = 0
    for i in range(n):
        if grid[i][c] == temp:
            cnt += 1
        else:
            temp = grid[i][c]
            cnt = 1

        if cnt >= max_cnt:
            max_cnt = cnt

    if cnt >= m:
        happy += 1

print(happy)