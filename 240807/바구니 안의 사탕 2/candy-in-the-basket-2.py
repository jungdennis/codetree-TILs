n, k = map(int, input().split())

arr = [0] * 101
for i in range(n):
    cnt, idx = map(int, input().split())
    arr[idx] = cnt

import sys
max_candy = -sys.maxsize
for i in range(k+1, 100-k):
    candy = 0
    for j in range(-k, k+1):
        candy += arr[i+j]
    max_candy = max(max_candy, candy)

print(max_candy)