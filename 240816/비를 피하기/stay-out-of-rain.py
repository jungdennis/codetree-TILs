from collections import deque
import sys

n, h, m = map(int, input().split())

arr = []
people = []
shelter = []
for r in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

    for c in range(n):
        if row[c] == 2:
            people.append((r, c))
        if row[c] == 3:
            shelter.append((r, c))

q = deque()

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = 1
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))

ans = [[0 for i in range(n)] for j in range(n)]                
for r, c in people:
    visited = [[False for i in range(n)] for j in range(n)]
    step = [[-1 for i in range(n)] for j in range(n)]

    visited[r][c] = True
    step[r][c] = 0
    q.append((r, c))
    bfs()

    min_dist = sys.maxsize
    for r_, c_ in shelter:
        if step[r_][c_] != -1:
            min_dist = min(step[r_][c_], min_dist)
    
    if min_dist == sys.maxsize:
        ans[r][c] = -1
    else:
        ans[r][c] = min_dist

for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()