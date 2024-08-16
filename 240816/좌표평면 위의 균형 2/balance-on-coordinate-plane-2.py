import sys

n = int(input())

point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

min_m = sys.maxsize
for i in range(2, 102, 2):
    for j in range(2, 102, 2):
        cnt = [0] * 4

        for x, y in point:
            if x < i and y < j:
                cnt[0] += 1
            elif x < i and y > j:
                cnt[1] += 1
            elif x > i and y < j:
                cnt[2] += 1
            elif x >i and  y > j:
                cnt[3] += 1

        m = max(cnt)
        min_m = min(m, min_m)

print(min_m)