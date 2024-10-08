# 0, 1, 2, 3 : 북, 동, 남, 서
from collections import deque

R, C, K = map(int, input().split())

start = []
for i in range(K):
    c, d = map(int, input().split())
    start.append((c-1, d))


forest = [[0 for i in range(C)] for j in range(R+1)]
center = [(-1, -1)]
# exit = [[0 for i in range(C)] for j in range(R+1)]
exit = [(-1, -1)]

ans = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def in_range(r, c):
    return r >= 0 and r <= R and c >= 0 and c < C
def in_range_(r, c):
    return r <= R and c >= 0 and c < C

def can_down(r, c):
    if not in_range(r+1, c-1) or forest[r+1][c-1] != 0:
        return False
    elif not in_range(r+2, c) or forest[r+2][c] != 0:
        return False
    elif not in_range(r+1, c+1) or forest[r+1][c+1] != 0:
        return False

    return True

def can_left(r, c):
    if not in_range_(r-1, c-1) or forest[r-1][c-1] != 0:
        return False
    elif not in_range_(r, c-2) or forest[r][c-2] != 0:
        return False
    elif not in_range_(r+1, c-1) or forest[r+1][c-1] != 0:
        return False

    return True

def can_right(r, c):
    if not in_range_(r-1, c+1) or forest[r-1][c+1] != 0:
        return False
    elif not in_range_(r, c+2) or forest[r][c+2] != 0:
        return False
    elif not in_range_(r+1, c+1) or forest[r+1][c+1] != 0:
        return False

    return True 

for i in range(K):
    # 골렘 이동
    r = -1
    c, d = start[i]

    while True:
        if can_down(r, c):
            r += 1
        elif can_left(r, c) and can_down(r, c-1):
            r += 1
            c -= 1
            d -= 1
        elif can_right(r, c) and can_down(r, c+1):
            r += 1
            c += 1
            d += 1
        else:
            break
    
    forest[r][c] = i+1
    for j in range(4):
        nr, nc = r + dr[j], c + dc[j]

        if in_range(nr, nc):
            # if j == d % 4:
            #     forest[nr][nc] = 2
            # else:
            #     forest[nr][nc] = 1
            if j == d % 4:
                # exit[nr][nc] = i+1
                exit.append((nr, nc))
            forest[nr][nc] = i+1

    center.append((r, c))

    flag = True
    for j in range(C):
        if forest[0][j] != 0:
            forest = [[0 for _ in range(C)] for _ in range(R+1)]
            exit.append((-1, -1))
            flag = False
            # print('clear')
            break
            
    # print(f"<{i}>")
    # print(center)
    # print(exit)
    # for k in range(len(forest)):
    #     print(forest[k])

    if flag:
        visited = [True] + [False] * (i+1)

        q = deque()
        q.append(i+1)
        
        max_row = 0
        # print(visited)
        # print(center)
        # print(exit)

        while q:
            idx = q.popleft()
            visited[idx] = True
            c_r, c_c = center[idx]
            e_r, e_c = exit[idx]
            # print(c_r, c_c)

            max_row = max(c_r + 1, max_row)

            for j in range(4):
                nr, nc = e_r + dr[j], e_c + dc[j]
                if in_range(nr, nc) and forest[nr][nc] != 0 and not visited[forest[nr][nc]]:
                    q.append(forest[nr][nc])
                    # print(forest[nr][nc])

        # print(max_row)
        ans += max_row

print(ans)