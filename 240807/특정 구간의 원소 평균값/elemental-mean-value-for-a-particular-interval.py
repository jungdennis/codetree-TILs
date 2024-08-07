n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        arr_ = []
        for k in range(i, j+1):
            arr_.append(arr[k])

        avg = sum(arr_) / len(arr_)

        if avg in arr_:
            cnt += 1

print(cnt)