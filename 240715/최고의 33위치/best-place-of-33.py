import sys

N = int(sys.stdin.readline().rstrip())

grid = []
for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_coin = 0
for r in range(N):
    for c in range(N):
        if (r+2 >= N) or (c+2 >= N):
            pass
        else:
            coin = 0
            for i in range(r, r+3):
                for j in range(c, c+3):
                    coin += grid[i][j]

            if coin >= max_coin:
                max_coin = coin

print(max_coin)