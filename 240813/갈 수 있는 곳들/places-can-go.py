from collections import deque
import sys

n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False for i in range(n)] for j in range(n)]

q = deque()

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def bfs():
    global cnt

    while q:
        r, c = q.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] == 0:
                visited[nr][nc] = True
                q.append((nr, nc))
                cnt += 1

cnt = 0
for i in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    
    if in_range(r, c) and not visited[r][c] and arr[r][c] == 0:
        visited[r][c] = True
        q.append((r, c))
        cnt += 1
        bfs()

print(cnt)