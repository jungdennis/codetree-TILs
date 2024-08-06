n = int(input())
target_arr = []
for i in range(n):
    target_arr.append(list(map(int, input().split())))

target = []
for i in range(n):
    for j in range(n):
        if target_arr[i][j] == 1:
            target.append((i, j))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


max_cnt = 0
bomb_kind = []

def boom(target, kind):
    bombed = [[0 for i in range(n)] for j in range(n)]

    for t, k in zip(target, kind):
        x, y = t

        if k == 1:
            for i in range(-2, 3):
                if in_range(x+i, y):
                    bombed[x+i][y] = 1
        elif k == 2:
            for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]:
                if in_range(x+i, y+j):
                    bombed[x+i][y+j] = 1
        elif k == 3:
            for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]:
                if in_range(x+i, y+j):
                    bombed[x+i][y+j] = 1

    # print(kind)
    cnt = 0
    for i in range(n):
        for j in range(n):
            # print(bombed[i][j], end=' ')
            if bombed[i][j] == 1:
                cnt += 1
        # print()
    # print('\n')

    return cnt

def bomb(x):
    global bombed, debug

    if x >= len(target):
        global max_cnt

        cnt = boom(target, bomb_kind)
        max_cnt = max(max_cnt, cnt)

        return
        
    for k in [1, 2, 3]:
        bomb_kind.append(k)
        bomb(x+1)
        bomb_kind.pop()

bomb(0)
print(max_cnt)