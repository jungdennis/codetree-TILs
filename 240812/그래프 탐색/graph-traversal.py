import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [1, 1] + [0] * (n-1)
cnt = 0

def move(last_node):
    # if last_node not in approach:
    #     approach.append(last_node)
    # else:
    #     return
    global cnt

    for i in graph[last_node]:
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            move(i)

move(1)
# print(len(approach)-1)
print(cnt)