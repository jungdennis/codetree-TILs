import sys

n = int(input())

line = []
for i in range(n):
    start, end = map(int, input().split())
    line.append((start, end))

flag = False
for i in range(n):
    max_start = -sys.maxsize
    min_end = sys.maxsize

    for j in range(n):
        if j != i:
            start, end = line[j]
            max_start = max(start, max_start)
            min_end = min(end, min_end)

    if max_start <= min_end:
        flag = True
        break

print('Yes') if flag else print('No')