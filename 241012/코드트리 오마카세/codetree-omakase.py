from collections import deque

L, Q = map(int, input().split())

belt = deque([[] for i in range(L)])

now_time = 0

for _ in range(Q):
    order = input().split()

    dt = int(order[1]) - now_time
    for i in range(dt):
        belt.append(belt.popleft())

    if order[0] == '100':
        _, t, x, name = order
    elif order[0] == '200':
        _, t, x, name, n = order
    elif order[0] == '300':
        pass