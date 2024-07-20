n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
max_cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0

    max_cnt = max(cnt, max_cnt)
print(max_cnt)