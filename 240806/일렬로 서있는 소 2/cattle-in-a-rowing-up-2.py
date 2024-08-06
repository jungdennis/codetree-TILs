n = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    t1 = arr[i]
    for j in range(i+1, n):
        t2 = arr[j]
        for k in range(j+1, n):
            t3 = arr[k]

            if t1 <= t2 and t2 <= t3:
                cnt += 1

print(cnt)