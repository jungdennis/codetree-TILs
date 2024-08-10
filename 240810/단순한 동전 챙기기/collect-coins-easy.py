import sys

n = int(input())
arr = []

for i in range(n):
    arr.append(list(input()))

start = (0, 0)
end = (0, 0)

coin = []
for r in range(n):
    for c in range(n):
        if arr[r][c] == 'S':
            start = (r, c, 0)
        elif arr[r][c] == 'E':
            end = (r, c, 6)
        elif arr[r][c] != '.':
            coin.append((r, c, int(arr[r][c])))

coin.sort(key=lambda x:x[2])

picked = []
min_distance = sys.maxsize
def pick(n_pick, last_idx):
    if n_pick >= 3:
        global min_distance

        route = [start] + picked + [end]
        distance = 0

        for i in range(4):
            x1, y1, _ = route[i]
            x2, y2, _ = route[i+1]
            distance += (abs(x1 - x2) + abs(y1 - y2))

        print()
        min_distance = min(distance, min_distance)

    for i in range(len(coin)):
        if i <= last_idx:
            continue

        picked.append(coin[i])
        pick(n_pick + 1, i)
        picked.pop()

if len(coin) < 3:
    print(-1)
else:
    pick(0, -1)
    print(min_distance)