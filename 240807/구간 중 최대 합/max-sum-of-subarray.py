import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_result = -sys.maxsize
for i in range(n-k+1):
    result = 0
    # debug = []
    for j in range(k):
        result += arr[i+j]
        # debug.append(arr[i+j])
    # print(debug)

    max_result = max(max_result, result)

print(max_result)