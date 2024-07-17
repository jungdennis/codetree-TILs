import sys
N, M, Q = map(int, sys.stdin.readline().rstrip().split())
grid = []

for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

def wind(row, direction):
    if direction == "L":
        temp = grid[row][-1]
        for i in range(M - 1, 0, -1):
            grid[row][i] = grid[row][i-1]
        grid[row][0] = temp
    elif direction == "R":
        temp = grid[row][0]
        for i in range(M - 1):
            grid[row][i] = grid[row][i+1]
        grid[row][-1] = temp

def change_direction(direction):
    if direction == "L":
        return "R"
    elif direction == "R":
        return "L"

for t in range(Q):
    row, direction = sys.stdin.readline().rstrip().split()
    row = int(row) - 1

    # 최초
    wind(row, direction)

    # for i in range(N):
    #     for j in range(M):
    #         print(grid[i][j], end=' ')
    #     print()
    # print('\n')

    # 전파 - 위쪽
    row_up = row-1
    dir_up = change_direction(direction)
    while row_up >= 0:
        flag = False

        for j in range(M):
            if grid[row_up][j] == grid[row_up+1][j]:
                flag = True
                break

        if flag:
            wind(row_up, dir_up)
            # for i in range(N):
            #     for j in range(M):
            #         print(grid[i][j], end=' ')
            #     print()
            # print('\n')

            row_up -= 1
            dir_up = change_direction(dir_up)
        else:
            break


    # 전파 - 아랫쪽
    row_down = row+1
    dir_down = change_direction(direction)
    while row_down < N:
        flag = False

        for j in range(M):
            if grid[row_down][j] == grid[row_down-1][j]:
                flag = True
                break

        if flag:
            wind(row_down, dir_down)
            # for i in range(N):
            #     for j in range(M):
            #         print(grid[i][j], end=' ')
            #     print()
            # print('\n')

            row_down += 1
            dir_down = change_direction(dir_down)
        else:
            break

for i in range(N):
    for j in range(M):
        print(grid[i][j], end=' ')
    print()