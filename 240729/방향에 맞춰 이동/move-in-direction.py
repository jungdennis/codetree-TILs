N = int(input())

dd = ['W', 'S', 'N', 'E']
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0

for i in range(N):
    d, n = input().split()

    n = int(n)

    for i in range(len(dd)):
        if d == dd[i]:
            x, y = x + n * dx[i], y + n * dy[i]

print(x, y)