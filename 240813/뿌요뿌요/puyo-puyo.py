import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False for i in range(n)] for j in range(n)]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def move(r, c):
    global cnt

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
            cnt += 1
            visited[nr][nc] = True

            move(nr, nc)

bomb = 0
max_cnt = -sys.maxsize
for r in range(n):
    for c in range(n):
        if in_range(r, c) and not visited[r][c]:
            cnt = 1
            visited[r][c] = True
            move(r, c)

            if cnt >= 4:
                bomb += 1
                max_cnt = max(cnt, max_cnt)

print(bomb, max_cnt)