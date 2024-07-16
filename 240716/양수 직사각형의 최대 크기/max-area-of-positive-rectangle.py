import sys

def find_square(grid, h, w, r, c):
    cnt = 0
    if (r+h-1 >= n) or (c+w-1 >= m):
        return 0
    else:
        for i in range(h):
            for j in range(w):
                if grid[r+i][c+j] <= 0:
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
        for h in range(1, n+1):
            for w in range(1, m+1):
                cnt = find_square(grid, h, w, r, c)
                # if cnt != 0:
                #     print(h, w, r, c, cnt)
                if cnt > max_cnt:
                    max_cnt = cnt

print(max_cnt)