import sys

def find_square(grid, n, m, r, c):
    max_r = n - r
    max_c = m - c
    
    cnt = 0
    for i in range(max_r):
        for j in range(max_c):
            if grid[r+i][c+j] <=0:
                return 0
            else:
                cnt += 1
    
    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_cnt = 0
for r in range(n):
    for c in range(m):
        cnt = find_square(grid, n, m, r, c)

        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)