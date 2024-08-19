import sys
N, M = map(int, input().split())

arr = []
for i in range(M):
    a, b = map(int, input().split())
    arr.append((a, b))

max_cnt = -sys.maxsize
for x in range(1, N+1):
    for y in range(1, N+1):
        if x == y:
            continue

        cnt = 0
        for a, b in arr:
            if (x == a and y == b) or (x == b and y == a):
                cnt += 1

        max_cnt = max(cnt, max_cnt)

print(max_cnt)