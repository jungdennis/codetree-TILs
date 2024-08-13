import sys
sys.setrecursionlimit(3000)

n, m = map(int, input().split())

arr = []
max_h = 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

    max_h = max(max_h, max(row))

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def move(r, c, k):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] > k:
            visited[nr][nc] = True
            move(nr, nc, k)

max_k = -sys.maxsize
max_zone = -sys.maxsize
for k in range(1, max_h + 1):
    zone = 0
    visited = [[False for i in range(m)] for j in range(n)]

    for r in range(n):
        for c in range(m):
            if in_range(r, c) and not visited[r][c] and arr[r][c] > k:
                zone += 1
                visited[r][c] = True
                move(r, c, k)

    if zone > max_zone:
        max_k = k
        max_zone = zone
                
print(max_k, max_zone)