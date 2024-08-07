n, k = map(int, input().split())

arr = [0] * 101
for i in range(n):
    cnt, idx = map(int, input().split())
    arr[idx] = cnt

import sys
max_candy = -sys.maxsize
for c in range(k+1, 100-k):
    candy = sum(arr[c-k:c+k+1])
    max_candy = max(max_candy, candy)

print(max_candy)