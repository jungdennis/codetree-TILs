n, k, p, t = map(int, input().split())

virus = [-1] + [0 for i in range(n)]
spread = [-1] + [0 for i in range(n)]

virus[p] = 1

shake_info = []

for i in range(t):
    shake_info.append(list(map(int, input().split())))

shake_info.sort(key=lambda x: x[0])

for t, x, y in shake_info:
    if virus[x] == 1 and spread[x] <= k:
        spread[x] += 1
        virus[y] = 1

for i in range(1, n+1):
    print(virus[i], end='')