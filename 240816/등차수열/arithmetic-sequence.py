import sys

n = int(input())
arr = list(map(int, input().split()))

max_cnt = -sys.maxsize
for k in range(101):
    cnt = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if k - arr[i] == arr[j] - k:
                cnt += 1

    max_cnt = max(cnt, max_cnt)

print(max_cnt)