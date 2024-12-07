from collections import deque

drs = [-1, 0, 1, 0]
dcs = [0, -1, 0, 1]

L, N, Q = map(int, input().split())

arr = []
for i in range(L):
    arr.append(list(map(int, input().split())))

arr_knights = [[0 for i in range(L)] for j in range(L)]
knights = [0 for i in range(N+1)]
barrier = [0 for i in range(N+1)]
hp = [0 for i in range(N+1)]
survived = [False] + [True for i in range(N)]

for i in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1

    knights[i] = (r, c)
    barrier[i] = (h, w)
    hp[i] = k

    for dr in range(h):
        for dc in range(w):
            nr, nc = r + dr, c + dc
            arr_knights[nr][nc] = i

for i in range(L):
    print(arr[i])
print()
for i in range(L):
    print(arr_knights[i])

def in_range(r, c, h, w):
    for dr in range(h):
        for dc in range(w):
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= L or nc < 0 or nc >= L:
                return False

    return True

def is_wall(r, c, h, w):
    for dr in range(h):
        for dc in range(w):
            nr, nc = r + dr, c + dc

            if arr[nr][nc] == 2:
                return True

    return False

for _ in range(Q):
    print(_)
    i, d = map(int, input().split())
    move = deque()

    if survived[i]:
        r, c = knights[i]
        h, w = barrier[i]
        dr, dc = drs[d], dcs[d]
        nr, nc = r + dr, c + dc

        while True:
            if in_range(nr, nc, h, w) and not is_wall(nr, nc, h, w):
                move.append((i, (nr, nc)))
                print(move)

                new_i = i
                for i in range(h):
                    for j in range(w):
                        if arr_knights[nr][nc] != 0 and arr_knights[nr][nc] != i:
                            

                if arr_knights[nr][nc] != 0 and arr_knights[nr][nc] != i:
                    i = arr_knights[nr][nc]
                    nr, nc = nr + dr, nc + dc
                    h, w = barrier[i]
                else:
                    print(f'move end: {move}')
                    break
            else:
                move = deque()
                print(f'all stop: {move}')
                break


        print(move)
    


