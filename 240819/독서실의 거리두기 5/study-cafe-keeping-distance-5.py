import sys
n = int(input())

arr = list(map(int, list(input())))

max_dist = -sys.maxsize

def calc_dist():
    idx = []

    for i in range(n):
        if arr[i] == 1:
            idx.append(i)

    dist = sys.maxsize

    for i in range(len(idx)-1):
        dist = min(dist, abs(idx[i+1] - idx[i]))

    return dist

for i in range(n):
    if arr[i] == 1:
        continue
    elif arr[i] == 0:
        arr[i] = 1

        dist = calc_dist()
        max_dist = max(dist, max_dist)

        arr[i] = 0

print(max_dist)