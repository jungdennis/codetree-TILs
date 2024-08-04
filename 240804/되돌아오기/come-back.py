x, y = 0, 0

dd = ['W', 'S', 'N', 'E']
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cnt = 0

n = int(input())
for i in range(n):
    d, t = input().split()
    t = int(t)

    j = dd.index(d)
    for _ in range(t):
        x, y = x + dx[j], y + dy[j]
        cnt += 1

        if (x, y) == (0, 0):
            break

    if (x, y) == (0, 0):
        break
    elif i == n-1:
        cnt = -1

print(cnt)