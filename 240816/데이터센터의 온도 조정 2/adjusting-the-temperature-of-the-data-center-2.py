import sys

N, C, G, H = map(int, input().split())

th = []
for i in range(N):
    a, b = map(int, input().split())
    th.append((a, b))

max_work = -sys.maxsize
for t in range(1001):
    work = 0

    for t_a, t_b in th:
        if t < t_a:
            work += C
        elif t <= t_b:
            work += G
        else:
            work += H

    max_work = max(work, max_work)

print(max_work)