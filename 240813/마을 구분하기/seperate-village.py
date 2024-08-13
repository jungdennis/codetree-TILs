n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False for i in range(n)] for j in range(n)]
village = []

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def move(r, c):
    global cnt

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] == 1:
            cnt += 1
            # picked.append((nr, nc))
            visited[nr][nc] = True

            move(nr, nc)

for r in range(n):
    for c in range(n):
        if in_range(r, c) and not visited[r][c] and arr[r][c] == 1:
            cnt = 1
            # picked = [(r, c)]
            visited[r][c] = True

            move(r, c)

            village.append(cnt)
            # village.append(picked)

village.sort()
print(len(village))
for n in village:
    print(n)