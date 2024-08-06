n, t = map(int, input().split())
order = input()

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

r, c = n // 2, n // 2
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
delta = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

score = arr[r][c]
for o in order:
    if o == 'L':
        delta += 1
    elif o == 'R':
        delta -= 1
    elif o == 'F':
        nr, nc = r + dr[delta % 4], c + dc[delta % 4]

        if in_range(nr, nc):
            r, c = nr, nc
            score += arr[r][c]

print(score)