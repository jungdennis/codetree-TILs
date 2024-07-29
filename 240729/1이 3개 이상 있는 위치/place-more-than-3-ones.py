n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

cnt = 0
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

for r in range(n):
    for c in range(n):
        one = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and arr[nr][nc] == 1:
                one += 1

        if one >= 3:
            cnt += 1

print(cnt)