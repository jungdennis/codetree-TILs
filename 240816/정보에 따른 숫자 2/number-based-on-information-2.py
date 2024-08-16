import sys

T, a, b = map(int, input().split())

arr = []
for i in range(T):
    c, n = input().split()
    n = int(n)
    arr.append((n, c))

beautiful = 0
for k in range(a, b+1):
    dist_S = sys.maxsize
    dist_N = sys.maxsize

    for n, c in arr:
        if c == 'S':
            dist_S = min(abs(n-k), dist_S)
        elif c == 'N':
            dist_N = min(abs(n-k), dist_N)

    if dist_S <= dist_N:
        beautiful += 1

print(beautiful)