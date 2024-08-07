n = int(input())
arr = list(map(int, input().split()))

import sys
max_sum = -sys.maxsize
for i in range(n):
    for j in range(i+2, n):
        max_sum = max(max_sum, arr[i]+arr[j])

print(max_sum)