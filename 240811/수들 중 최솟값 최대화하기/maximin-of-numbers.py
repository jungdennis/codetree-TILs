import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

picked = []
visited = [0] * n

max_min = -sys.maxsize
def pick(x):
    if x >= n:
        global max_min

        min_ = sys.maxsize
        for r, c in enumerate(picked):
            min_ = min(arr[r][c], min_)
        
        max_min = max(min_, max_min)

        return

    for c in range(n):
        if visited[c] == 1:
            continue

        picked.append(c)
        visited[c] = 1

        pick(x+1)

        picked.pop()
        visited[c] = 0

pick(0)
print(max_min)