import sys

n, m = map(int, input().split())

arr = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1

visited = [1, 1] + [0] * (n-1)
node = []
max_node = -sys.maxsize

def move(last_node):
    global max_node
    print(node)
    max_node = max(len(node), max_node)

    for i in range(1, n+1):
        if arr[last_node][i] == 1 and visited[i] == 0:
            node.append(i)
            visited[i] = 1

            move(i)

            node.pop()
            visited[i] = 0

move(1)
print(max_node)