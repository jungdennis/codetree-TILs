from collections import deque
import sys

knight = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

visited = [[False for i in range(n)] for j in range(n)]
step = [[-1 for i in range(n)] for j in range(n)]

q = deque()

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in knight:
            nr, nc = r + dr, c +dc

            if in_range(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))

visited[r1][c1] = True
step[r1][c1] = 0
q.append((r1, c1))
bfs()

print(step[r2][c2])