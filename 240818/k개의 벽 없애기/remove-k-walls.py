import sys
from collections import deque

n, k = map(int, input().split())

arr = []
wall = []
for r in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

    for c in range(len(row)):
        if row[c] == 1:
            wall.append((r, c))

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

wall_pick = []
min_dist = sys.maxsize

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def pick_wall(n_pick):
    if n_pick >= k:
        global min_dist

        step = find_route()

        dist = step[r2][c2]
        # print(wall_pick, dist)
        # for i in range(n):
        #     print(step[i])
        if dist != -1:
            min_dist = min(dist, min_dist)

        return

    for (r, c) in wall:
        if (r, c) in wall_pick:
            continue

        wall_pick.append((r, c))
        arr[r][c] = 0

        pick_wall(n_pick+1)

        wall_pick.pop()
        arr[r][c] = 1

def find_route():
    visited = [[False for i in range(n)] for j in range(n)]
    step = [[-1 for i in range(n)] for j in range(n)]
    q = deque()

    visited[r1][c1] = True
    step[r1][c1] = 0
    q.append((r1, c1))

    while q:
        r, c = q.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] == 0:
                visited[nr][nc] = True
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))
    
    return step

    

pick_wall(0)

if min_dist == sys.maxsize:
    min_dist = -1
print(min_dist)