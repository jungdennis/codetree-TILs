n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]

dd = [0, 1, 2, 3]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

r = 0
c = 0
i = 0
for x in range(1, n*m+1):
    arr[r][c] = x

    nr, nc = r + dr[i % 4], c + dc[i % 4]
    if not in_range(nr, nc) or arr[nr][nc] != 0:
        i += 1
        nr, nc = r + dr[i % 4], c + dc[i % 4]
        
    r, c = nr, nc
    
        

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()