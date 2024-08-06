order = input()
t = 0
x, y = 0, 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
delta = 0

for o in order:
    if o == 'L':
        delta += 1
        t += 1
    elif o == 'R':
        delta -= 1
        t += 1
    elif o == 'F':
        x, y = x+dx[delta%4], y+dy[delta%4]
        t += 1

        if x == 0 and y == 0:
            break

if x != 0 and y != 0:
    t = -1

print(t)