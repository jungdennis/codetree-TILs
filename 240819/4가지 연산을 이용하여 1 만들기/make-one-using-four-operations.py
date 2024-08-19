import sys
from collections import deque

n = int(input())
max_n = 1000000
q = deque()
visited = [False for i in range(max_n + 1)]

def calc(n, x):
    if x == 0:
        return n + 1
    elif x == 1:
        return n - 1
    elif x == 2:
        return n // 2
    elif x == 3:
        return n // 3

def in_range(x):
    return x >= 0 and x <= max_n

def bfs():
    while q:
        x, cnt = q.popleft()

        if x == 1:
            return cnt
        else:
            calc_list = [0, 1]
            if x % 2 == 0:
                calc_list.append(2)
            if x % 3 == 0:
                calc_list.append(3)

            for c in calc_list:
                nx = calc(x, c)
                
                if in_range(nx) and not visited[nx]:
                    visited[nx] = True
                    q.append((nx, cnt + 1))

q.append((n, 0))
visited[n] = True
cnt = bfs()
print(cnt)