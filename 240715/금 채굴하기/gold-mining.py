import sys

def gold_mine(grid, n, m, k):
    max_gold = 0
    for r in range(n):
        for c in range(m):
            gold = 0

            for i in range(-k, k+1):
                for j in range(-k, k+1):
                    try:
                        gold += grid[r+i][c+j]
                    except:
                        pass

            if gold > max_gold:
                max_gold = gold

    return max_gold

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = []

for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

k = 0
max_gold = 0

while 1:
    cost = (k ** 2) + ((k + 1) ** 2)
    gold = gold_mine(grid, n, m, k)
    if gold * m < cost:
        break
    else:
        if gold > max_gold:
            max_gold = gold
        k += 1

print(max_gold)