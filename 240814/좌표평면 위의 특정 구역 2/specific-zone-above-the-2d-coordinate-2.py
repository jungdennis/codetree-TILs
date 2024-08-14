import sys

n = int(input())
point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

min_pad = sys.maxsize
for i in range(n):
    max_x, max_y = -sys.maxsize, -sys.maxsize
    min_x, min_y = sys.maxsize, sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        x, y = point[j]

        max_x, max_y = max(x, max_x), max(y, max_y)
        min_x, min_y = min(x, min_x), min(y, min_y)

    pad = (max_x - min_x) * (max_y - min_y)
    min_pad = min(pad, min_pad)

print(min_pad)