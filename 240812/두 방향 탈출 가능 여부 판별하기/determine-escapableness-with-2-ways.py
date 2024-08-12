import sys

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited =[[0 for i in range(m)] for j in range(n)]

ganeung = 0

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def can_go(r, c):
    if not in_range(r, c) or visited[r][c] == 1 or arr[r][c] == 0:
        return False
    else:
        return True

def move(r, c):
    global ganeung

    if r == n-1 and c == m-1:
        ganeung = 1
        sys.exit()

    visited[r][c] = 1

    for dr, dc in [(1, 0), (0, 1)]:
        nr, nc = r + dr, c + dc

        if can_go(nr, nc):
            move(nr, nc)

move(0, 0)
print(ganeung)