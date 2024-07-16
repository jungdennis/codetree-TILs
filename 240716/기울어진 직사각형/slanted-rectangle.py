import sys

def earn_score(n, grid, r, c, h, w):
    score = grid[r][c]
    r_now = r
    c_now = c

    for i in range(w):
        r_now -= 1
        c_now += 1

        if (r_now < 0) or (r_now >= n) or (c_now < 0) or (c_now >= n):
            return 0
        else:
            score += grid[r_now][c_now]

    for j in range(h):
        r_now -= 1
        c_now -= 1

        if (r_now < 0) or (r_now >= n) or (c_now < 0) or (c_now >= n):
            return 0
        else :
            score += grid[r_now][c_now]

    for i in range(w):
        r_now += 1
        c_now -= 1

        if (r_now < 0) or (r_now >= n) or (c_now < 0) or (c_now >= n):
            return 0
        else :
            score += grid[r_now][c_now]

    for j in range(h):
        r_now += 1
        c_now += 1

        if (r_now < 0) or (r_now >= n) or (c_now < 0) or (c_now >= n):
            return 0

    return score


n = int(sys.stdin.readline().rstrip())
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_score = 0
for r in range(n):
    for c in range(n):
        for h in range(1, n):
            for w in range(1, n):
                score = earn_score(n, grid, r, c, h, w)

                if score > max_score:
                    max_score = score

print(max_score)