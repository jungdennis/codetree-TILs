import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_result = -sys.maxsize
for i in range(n-k):
    result = 0
    for j in range(k):
        result += arr[i+j]

    max_result = max(max_result, result)

print(max_result)