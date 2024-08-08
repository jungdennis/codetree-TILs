n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

direction = []
for i in range(n):
    direction.append(list(map(int, input().split())))


dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

r, c = map(int, input().split())
r -= 1
c -= 1
moves = [(r, c)]

max_cnt = 0

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def detect(r, c):
    possible = []

    nr, nc = r, c
    d = direction[r][c]

    while in_range(nr, nc):
        nr, nc = nr + dr[d], nc + dc[d]
        if not in_range(nr, nc):
            break
        elif arr[nr][nc] > arr[r][c]:
            possible.append((nr, nc))

    return possible

def move(x):
    global max_cnt

    nr, nc = moves[-1]
    possible = detect(nr, nc)
    # print((nr, nc), possible)

    max_cnt = max(max_cnt, x)

    if len(possible) == 0:
        return
    
    for pr, pc in possible:
        moves.append((pr, pc))
        move(x+1)
        moves.pop()

move(0)
print(max_cnt)