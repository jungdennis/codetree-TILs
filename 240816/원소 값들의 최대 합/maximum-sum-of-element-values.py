import sys

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_sum = -sys.maxsize

for i in range(n):
    idx = i
    sum_ = 0
    for _ in range(m):
        sum_ += arr[idx]
        idx = arr[idx]

    max_sum = max(sum_, max_sum)

print(max_sum)