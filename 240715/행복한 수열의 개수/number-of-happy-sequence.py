import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
happy = 0
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

for r in range(n):
    max_cnt = 1
    cnt = 1
    # print(f"<row {r}>")
    for j in range(n):
        if j+1 >= n:
            continue

        if grid[r][j] == grid[r][j+1]:
            cnt += 1
        elif grid[r][j] != grid[r][j+1]:
            cnt = 1

        if cnt >= m:
            happy += 1
            break

    #     print(f"{grid[r][j]} - {grid[r][j+1]} : {cnt}, {max_cnt}")
    # print(f"row {r}:{max_cnt}")

for c in range(n):
    max_cnt = 1
    cnt = 1
    # print(f"<col {c}>")
    for i in range(n):
        if i+1 >= n:
            continue

        if grid[i][c] == grid[i+1][c]:
            cnt += 1
        elif grid[i][c] != grid[i+1][c]:
            cnt = 1

        if cnt >= m:
            happy += 1
            break
                
    #     print(f"{grid[i][c]} - {grid[i+1][c]} : {cnt}, {max_cnt}")
    # print(f"col {c}:{max_cnt}")

print(happy)