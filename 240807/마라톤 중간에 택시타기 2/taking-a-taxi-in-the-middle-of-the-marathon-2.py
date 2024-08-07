n = int(input())

ckpt = []
for i in range(n):
    x, y = map(int, input().split())
    ckpt.append((x, y))

max_distance = 99999999999
for i in range(1, n-1):
    distance = 0
    last_x, last_y = ckpt[0]

    for j in range(1, n):
        if i != j:
            x, y = ckpt[j]
            distance += (abs(last_x - x) + abs(last_y - y))
            last_x, last_y = x, y

    max_distance = min(max_distance, distance)

print(max_distance)