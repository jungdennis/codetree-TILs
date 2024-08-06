n, m = map(int, input().split())

arr = [[0 for i in range(m)] for j in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
delta = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

r, c = 0, 0 
for num in range(1, n*m+1):
    arr[r][c] = num

    nr, nc = r + dr[delta % 4], c + dc[delta % 4]
    if in_range(nr, nc) and arr[nr][nc] == 0:
        r, c = nr, nc
    else:
        delta += 1
        r, c = r + dr[delta % 4], c + dc[delta % 4]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()