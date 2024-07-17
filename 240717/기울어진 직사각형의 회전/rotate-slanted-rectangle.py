import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

r, c, m1, m2, m3, m4, dir = map(int, sys.stdin.readline().rstrip().split())
r -= 1
c -= 1

temp = arr[r][c]

if dir == 0:        # 반시계 방향
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]

    r_ = r
    c_ = c

    for i in range(m4):
        arr[r_][c_] = arr[r_+dr[0]][c_+dc[0]]

        r_ += dr[0]
        c_ += dc[0]

    for i in range(m3):
        arr[r_][c_] = arr[r_+dr[1]][c_+dc[1]]

        r_ += dr[1]
        c_ += dc[1]

    for i in range(m2):
        arr[r_][c_] = arr[r_+dr[2]][c_+dc[2]]

        r_ += dr[2]
        c_ += dc[2]

    for i in range(m1-1):
        arr[r_][c_] = arr[r_+dr[3]][c_+dc[3]]

        r_ += dr[3]
        c_ += dc[3]

    arr[r_][c_] = temp
elif dir == 1:      # 시계 방향
    dr = [-1, -1, 1, 1]
    dc = [1, -1, -1, 1]

    r_ = r
    c_ = c

    for i in range(m1):
        arr[r_][c_] = arr[r_+dr[0]][c_+dc[0]]

        r_ += dr[0]
        c_ += dc[0]

    for i in range(m2):
        arr[r_][c_] = arr[r_+dr[1]][c_+dc[1]]

        r_ += dr[1]
        c_ += dc[1]

    for i in range(m3):
        arr[r_][c_] = arr[r_+dr[2]][c_+dc[2]]

        r_ += dr[2]
        c_ += dc[2]

    for i in range(m4-1):
        arr[r_][c_] = arr[r_+dr[3]][c_+dc[3]]

        r_ += dr[3]
        c_ += dc[3]

    arr[r_][c_] = temp

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()