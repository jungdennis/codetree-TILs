import sys

n, b = map(int, input().split())
price = []
for i in range(n):
    price.append(int(input()))

max_cnt = -sys.maxsize
for i in range(n):
    price[i] = price[i] // 2
    spend = 0
    cnt = 0

    for p in sorted(price):
        if spend + p <= b:
            spend += p
            cnt += 1
        else:
            break

    max_cnt = max(cnt, max_cnt)
    price[i] = price[i] * 2

print(max_cnt)