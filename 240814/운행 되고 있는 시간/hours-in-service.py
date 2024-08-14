import sys

n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

max_working = -sys.maxsize
for i in range(n):
    working = [0] * 1001

    for j in range(n):
        if i == j:
            continue

        start, end = arr[j]

        for k in range(start, end):
            working[k] += 1

    working_time = 0
    for t in working:
        if t > 0:
            working_time += 1

    max_working = max(working_time, max_working)

print(max_working)