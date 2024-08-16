from collections import deque
import sys

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False for i in range(m)] for j in range(n)]
step = [[-1 for i in range(m)] for j in range(n)]

q = deque()

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))
                step[nr][nc] = step[r][c] + 1

step[0][0] = 0
visited[0][0] = True
q.append((0, 0))
bfs()
print(step[n-1][m-1])