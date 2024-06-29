from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
dq = deque()

for i in range(1, N+1):
    dq.append(i)

while True:
    dq.popleft()
    dq.append(dq.popleft())

    if len(dq) == 1:
        break

print(dq[0])