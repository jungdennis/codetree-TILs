import sys

def gold_mine(grid, n, k):
    max_gold = 0
    for r in range(n):
        for c in range(n):
            gold = 0
            grid_list = []
            for j in range(-k, k+1):
                r_range = k - abs(j)
                for i in range(-r_range, r_range+1):
                    if (r+i < 0) or (r+i >= n) or (c+j < 0) or (c+j >= n):
                        pass
                    else:
                        gold += grid[r+i][c+j]
                        grid_list.append((r+i, c+j))
            # print(f"({r}, {c}) : {gold} - {grid_list}")
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
    gold = gold_mine(grid, n, k)
    # print(f"{k}, {gold}, {cost // m +1}")
    if gold * m >= cost:
        if gold > max_gold:
            max_gold = gold
        k += 1
    else:
        break

print(max_gold)