import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

picked = []
visited = [1, 1] + [0] * (n-1)
min_score = sys.maxsize

def pick(x):
    if x >= n - 1:
        global min_score

        score = 0
        route = [1] + picked + [1]

        for i in range(len(route) - 1):
            start = route[i] - 1
            end = route[i+1] - 1
            score += arr[start][end]

        min_score = min(score, min_score)

        return

    for i in range(2, n+1):
        if visited[i] == 1:
            continue

        picked.append(i)
        visited[i] = 1

        pick(x+1)

        picked.pop()
        visited[i] = 0

pick(0)
print(min_score)