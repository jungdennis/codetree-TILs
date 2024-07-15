import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = []

for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_sum = 0

# L자
for i in range(n):
    for j in range(m):
        if (i+1 >= n) or (j+1 >= m):
            continue

        s1 = grid[i][j] + grid[i+1][j] + grid[i][j+1]
        s2 = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
        s3 = grid[i][j] + grid[i][j+1] + grid[i+1][j+1]
        s4 = grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]

        s_max = max(s1, s2, s3, s4)

        if s_max > max_sum:
            max_sum = s_max

# 가로 일자
for i in range(n):
    for j in range(m):
        if (j+2 >= n):
            continue

        s_row = grid[i][j] + grid[i][j+1] + grid[i][j+2]

        if s_row > max_sum:
            max_sum = s_row

# 세로 일자
for i in range(n):
    for j in range(m):
        if (i+2 >= n):
            continue

        s_col = grid[i][j] + grid[i+1][j] + grid[i+2][j]

        if s_col > max_sum:
            max_sum = s_col

print(max_sum)