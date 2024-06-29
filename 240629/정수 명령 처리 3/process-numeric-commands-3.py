from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
dq = deque()

for i in range(N):
    order = sys.stdin.readline().rstrip()

    if 'push' in order:
        A = int(order.split()[-1])
        if 'front' in order:
            dq.appendleft(A)
        elif 'back' in order:
            dq.append(A)
    elif 'pop' in order:
        if 'front' in order:
            print(dq.popleft())
        elif 'back' in order:
            print(dq.pop())
    elif 'size' in order:
        print(len(dq))
    elif 'empty' in order:
        print(1 if not dq else 0)
    elif 'front' in order:
        print(dq[0])
    elif 'back' in order:
        print(dq[-1])