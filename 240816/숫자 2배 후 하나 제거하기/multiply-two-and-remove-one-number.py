import sys

n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    arr[i] = arr[i] * 2

    for j in range(n):
        if i == j:
            continue

        arr_diff = arr[:j] + arr[j+1:]
        diff = 0
        for k in range(n-2):
            diff += abs(arr_diff[k] - arr_diff[k+1])

        min_diff = min(diff, min_diff)

    arr[i] = arr[i] // 2

print(min_diff)