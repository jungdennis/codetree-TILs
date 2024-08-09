n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = sum(arr)

import sys
min_diff = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        sum_ = arr_sum - (arr[i] + arr[j])
        diff = abs(s - sum_)

        min_diff = min(diff, min_diff)

print(min_diff)