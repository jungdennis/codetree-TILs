n, k, p, t = map(int, input().split())

virus = [-1] + [0 for i in range(n)]
spread = [-1] + [0 for i in range(n)]

virus[p] = 1

shake_info = []
for i in range(t):
    shake_info.append(list(map(int, input().split())))
shake_info.sort(key=lambda x: x[0])

for t, x, y in shake_info:
    info = []

    if virus[x] == 1 and spread[x] < k:
        info.append((x, y))
    if virus[y] == 1 and spread[y] < k:
        info.append((y, x))

    for s, v in info:
        spread[s] += 1
        virus[v] = 1

    # print(t, x, y, virus[1:], spread[1:])

for i in range(1, n+1):
    print(virus[i], end='')