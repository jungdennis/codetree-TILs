n, k = map(int, input().split())

arr = [0] * 101
for i in range(n):
    cnt, idx = map(int, input().split())
    arr[idx] += cnt

import sys
max_candy = -sys.maxsize
for c in range(101 - 2*k + 1):
    candy = sum(arr[c:c+2*k+1])
    # print((c, c+2*k), arr[c:c+2*k+1], candy)
    max_candy = max(max_candy, candy)

print(max_candy)