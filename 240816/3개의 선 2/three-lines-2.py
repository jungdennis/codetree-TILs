n = int(input())

point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

flag = 0
for i in range(11):
    for j in range(11):
        for k in range(11):
            cnt = 0
            for x, y in point:
                if x == i or x == j or y == k:
                    cnt += 1
            if cnt == n:
                flag = 1

            cnt = 0
            for x, y in point:
                if x == i or y == j or y == k:
                    cnt += 1
            if cnt == n:
                flag = 1

print(flag)