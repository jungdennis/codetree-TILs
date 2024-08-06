n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]

r, c = 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
delta = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for num in range(n*m):
    alphabet = chr((num % 26) + 65)

    arr[r][c] = alphabet

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