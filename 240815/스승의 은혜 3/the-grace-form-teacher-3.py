import sys

n, b = map(int, input().split())

price = []
ship = []
for i in range(n):
    p, s = map(int, input().split())
    price.append(p)
    ship.append(s)

max_cnt = -sys.maxsize
for i in range(n):
    total = []
    for j in range(n):
        if i == j:
            total.append(price[j] // 2 + ship[j])
        else:
            total.append(price[j] + ship[j])

    spend = 0
    cnt = 0
    for p in sorted(total):
        if spend + p <= b:
            spend += p
            cnt += 1
        else:
            break

    max_cnt = max(cnt, max_cnt)

print(max_cnt)