from collections import deque
import sys

queue = deque()

N, k = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, N+1):
    queue.append(i)

while len(queue) != 0:
    for j in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=" ")