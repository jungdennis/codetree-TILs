import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

picked = []
visited = [0] * n
max_score = -sys.maxsize

def pick(x):
    if x >= n:
        global max_score
        
        score = 0
        for r, c in enumerate(picked):
            score += arr[r][c]

        max_score = max(score, max_score)

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
print(max_score)