import sys

n = int(input())

arr = list(map(int, list(input())))

available = []
for i in range(n):
    if arr[i] == 0:
        available.append(i)

max_dist = -sys.maxsize
for i in available:
    for j in available:
        if i == j:
            continue

        arr[i] = 1
        arr[j] = 1

        seated = []
        for k in range(n):
            if arr[k] == 1:
                seated.append(k)

        dist = sys.maxsize
        for i in range(len(seated) - 1):
            dist = min(dist, seated[i+1] - seated[i])
        
        # print(dist, arr, seated)

        if dist > max_dist:
            max_dist = max(dist, max_dist)

        arr[i] = 0
        arr[j] = 0

print(max_dist)