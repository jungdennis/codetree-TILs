n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)

def in_range(x, y):
    return x >= 1 and x < n+1 and y >= 1 and y < n+1

dd = ['D', 'R', 'L', 'U']
dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]

i = dd.index(d)
for _ in range(t):
    nr, nc = r + dr[i], c + dc[i]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        i = 3 - i

print(r, c)