import sys

n, m = map(int, input().split())
point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))
picked = []

min_dist = sys.maxsize
def pick(n_pick, last_idx):
    if n_pick >= m:
        global min_dist
        dist = 0

        for i in range(m):
            x1, y1 = picked[i]
            for j in range(i+1, m):
                x2, y2 = picked[j]

                dist = max(dist, ((x1 - x2) ** 2) + ((y1 - y2) ** 2))

        min_dist = min(dist, min_dist)

        return


    for i in range(n):
        if i <= last_idx:
            continue

        picked.append(point[i])
        pick(n_pick + 1, i)
        picked.pop()

pick(0, -1)
print(min_dist)