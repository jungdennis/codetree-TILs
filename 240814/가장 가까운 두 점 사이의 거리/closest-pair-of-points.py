import sys

n = int(input())

point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

min_dist = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = point[i]
        x2, y2 = point[j]

        dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        min_dist = min(dist, min_dist)

print(min_dist)