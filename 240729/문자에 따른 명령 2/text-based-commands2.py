order = input()

x, y = 0, 0

state = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for o in order:
    if o == 'L':
        state += 1
    elif o == 'R':
        state -= 1
    elif o == 'F':
        i = state % 4
        x, y = x + dx[i], y + dy[i]

print(x, y)