import sys

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [1, 1] + [0] * (n-1)
node = []
approach = []

def move(last_node):
    if last_node != 1 and last_node not in approach:
        approach.append(last_node)

    for i in graph[last_node]:
        if visited[i] == 0:
            node.append(i)
            visited[i] = 1

            move(i)

            node.pop()
            visited[i] = 0

move(1)
print(len(approach))