import sys
from collections import deque

n = int(input())
q = deque()

def calc(n, x):
    if x == 0:
        return n + 1
    elif x == 1:
        return n - 1
    elif x == 2:
        return n // 2
    elif x == 3:
        return n // 3

def bfs():
    while q:
        n, cnt = q.popleft()

        if n == 1:
            return cnt
        else:
            calc_list = [0, 1]

            if n % 2 == 0:
                calc_list.append(2)
            if n % 3 == 0:
                calc_list.append(3)

            for c in calc_list:
                new_n = calc(n, c)
                q.append((new_n, cnt + 1))


q.append((n, 0))
cnt = bfs()
print(cnt)